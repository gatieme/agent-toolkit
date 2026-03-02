#!/usr/bin/env python3
"""
配置文件同步脚本

支持将本仓库配置文件更新到实际安装目录，或将实际安装目录的文件备份回当前仓库。

目录映射:
- opencode/  → ~/.config/opencode
- skills/    → ~/.agents/skills

功能:
- 更新模式: 从仓库选择一个配置文件（单选）更新到 ~/.config/opencode/oh-my-opencode.jsonc
- 备份模式: 从 ~/.config/opencode 选择多个配置文件（多选）备份到仓库 opencode/ 目录
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.shortcuts import radiolist_dialog, checkboxlist_dialog, yes_no_dialog, message_dialog
from prompt_toolkit.styles import Style


class ConfigSync:
    """配置文件同步管理器"""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root.resolve()
        self.opencode_repo = self.repo_root / "opencode"
        self.opencode_target = Path.home() / ".config" / "opencode"
        self.target_file = "oh-my-opencode.jsonc"

        # 配置文件过滤模式
        self.config_patterns = [
            "oh-my-opencode.jsonc",
            "oh-my-opencode-*.jsonc",
            "oh-my-opencode-slim.json",
        ]

    def validate_paths(self) -> bool:
        """验证路径是否存在"""
        if not self.opencode_repo.exists():
            print(f"❌ 错误: 仓库 opencode 目录不存在: {self.opencode_repo}")
            return False

        if not self.opencode_target.exists():
            print(f"❌ 错误: 安装目录不存在: {self.opencode_target}")
            print(f"   请先创建目录: {self.opencode_target}")
            return False

        return True

    def discover_config_files(self, directory: Path) -> List[Path]:
        """
        发现目录中的配置文件

        Args:
            directory: 要搜索的目录

        Returns:
            配置文件列表
        """
        config_files = []

        if not directory.exists():
            return config_files

        for pattern in self.config_patterns:
            # 将 shell 风格的通配符转换为 glob 模式
            if '*' in pattern:
                # 提取前缀和后缀
                parts = pattern.split('*')
                prefix = parts[0]
                suffix = parts[1] if len(parts) > 1 else ''

                # 查找匹配的文件
                for file in directory.glob(f"{prefix}*{suffix}"):
                    if file.is_file() and file not in config_files:
                        config_files.append(file)
            else:
                file = directory / pattern
                if file.is_file() and file not in config_files:
                    config_files.append(file)

        return sorted(config_files, key=lambda x: x.name)

    def show_update_selector(self) -> Optional[Path]:
        """
        显示更新模式的选择界面（单选）

        Returns:
            用户选择的文件，如果取消则返回 None
        """
        config_files = self.discover_config_files(self.opencode_repo)

        if not config_files:
            message_dialog(
                title="未找到配置文件",
                text=f"在 {self.opencode_repo} 中未找到配置文件"
            ).run()
            return None

        # 构建选择列表
        choices = []
        for idx, file in enumerate(config_files):
            # 获取文件大小和修改时间
            size = file.stat().st_size
            mtime = file.stat().st_mtime
            import datetime
            mtime_str = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")

            # 判断是否是当前目标文件
            is_target = file.name == self.target_file
            marker = " [当前目标]" if is_target else ""

            choices.append((
                str(file),
                f"{file.name} ({size} bytes, {mtime_str}){marker}"
            ))

        # 显示单选对话框
        result = radiolist_dialog(
            title="选择要更新的配置文件",
            text=f"将选中的文件更新到: {self.opencode_target / self.target_file}",
            values=choices,
            cancel_text="取消"
        ).run()

        if result is None:
            return None

        return Path(result)

    def show_backup_selector(self) -> Optional[List[Path]]:
        """
        显示备份模式的选择界面（多选）

        Returns:
            用户选择的文件列表，如果取消则返回 None
        """
        config_files = self.discover_config_files(self.opencode_target)

        if not config_files:
            message_dialog(
                title="未找到配置文件",
                text=f"在 {self.opencode_target} 中未找到配置文件"
            ).run()
            return None

        # 构建选择列表
        choices = []
        for idx, file in enumerate(config_files):
            # 获取文件大小和修改时间
            size = file.stat().st_size
            mtime = file.stat().st_mtime
            import datetime
            mtime_str = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")

            # 检查仓库中是否已存在
            repo_file = self.opencode_repo / file.name
            exists_in_repo = repo_file.exists()
            marker = " [已存在]" if exists_in_repo else ""

            choices.append((
                str(file),
                f"{file.name} ({size} bytes, {mtime_str}){marker}"
            ))

        # 显示多选对话框
        result = checkboxlist_dialog(
            title="选择要备份的配置文件",
            text=f"将选中的文件备份到: {self.opencode_repo}",
            values=choices,
            cancel_text="取消"
        ).run()

        if result is None:
            return None

        return [Path(f) for f in result]

    def show_diff(self, src: Path, dst: Path) -> bool:
        """
        显示两个文件的差异

        Args:
            src: 源文件
            dst: 目标文件

        Returns:
            True 如果有差异，False 如果文件相同
        """
        print(f"\n{'='*80}")
        print(f"📊 差异比较")
        print(f"{'='*80}")
        print(f"源文件: {src}")
        print(f"目标文件: {dst}")
        print(f"{'='*80}\n")

        if not src.exists():
            print(f"❌ 源文件不存在: {src}")
            return False

        if not dst.exists():
            print(f"⚠️  目标文件不存在，将创建新文件")
            print(f"\n源文件内容预览 (前 30 行):")
            print("-" * 80)
            with open(src, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    if i > 30:
                        print(f"\n... (还有更多内容)")
                        break
                    print(f"{i:4d}: {line.rstrip()}")
            print("-" * 80)
            return True

        # 使用 diff 命令比较
        try:
            cmd = ["diff", "-u", str(dst), str(src)]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.repo_root
            )

            if result.returncode == 0:
                print("✅ 文件内容完全一致，无需更新")
                return False
            else:
                diff_lines = result.stdout.strip().split('\n')
                # 限制显示行数
                max_lines = 100
                if len(diff_lines) > max_lines:
                    print(f"差异输出较长，显示前 {max_lines} 行:")
                    print('\n'.join(diff_lines[:max_lines]))
                    print(f"\n... (还有 {len(diff_lines) - max_lines} 行差异)")
                else:
                    print(result.stdout)
                print("-" * 80)
                return True

        except FileNotFoundError:
            print("⚠️  diff 命令不可用，使用简单比较")
            # 读取文件内容
            with open(src, 'r', encoding='utf-8') as f:
                src_content = f.read()
            with open(dst, 'r', encoding='utf-8') as f:
                dst_content = f.read()

            if src_content == dst_content:
                print("✅ 文件内容完全一致，无需更新")
                return False
            else:
                print("⚠️  文件内容不同（diff 命令不可用，无法显示详细差异）")
                return True

    def confirm_action(self, action: str) -> bool:
        """
        确认用户操作

        Args:
            action: 操作描述

        Returns:
            用户是否确认
        """
        result = yes_no_dialog(
            title="确认操作",
            text=f"{action}\n\n确定要执行此操作吗？"
        ).run()

        return result

    def sync_file(self, src: Path, dst: Path) -> bool:
        """
        同步文件

        Args:
            src: 源文件
            dst: 目标文件

        Returns:
            是否成功
        """
        try:
            # 确保目标目录存在
            dst.parent.mkdir(parents=True, exist_ok=True)

            # 复制文件
            shutil.copy2(src(src), dst)
            return True

        except Exception as e:
            print(f"❌ 复制失败: {e}")
            return False

    def update(self) -> bool:
        """
        更新模式：从仓库选择一个配置文件更新到安装目录

        Returns:
            是否成功
        """
        print("\n🔄 更新模式：仓库 → 安装目录")
        print(f"仓库目录: {self.opencode_repo}")
        print(f"安装目录: {self.opencode_target}")
        print(f"目标文件: {self.target_file}\n")

        # 验证路径
        if not self.validate_paths():
            return False

        # 显示选择界面
        src_file = self.show_update_selector()
        if src_file is None:
            print("❌ 操作已取消")
            return False

        dst_file = self.opencode_target / self.target_file

        # 显示差异
        has_diff = self.show_diff(src_file, dst_file)
        if not has_diff:
            print("✅ 文件已是最新的，无需更新")
            return True

        # 确认操作
        action_desc = f"将 {src_file.name} 更新到 {dst_file}"
        if not self.confirm_action(action_desc):
            print("❌ 操作已取消")
            return False

        # 执行更新
        print(f"\n📋 正在更新...")
        if self.sync_file(src_file, dst_file):
            print(f"✅ 更新成功!")
            print(f"   源文件: {src_file}")
            print(f"   目标文件: {dst_file}")
            return True
        else:
            print(f"❌ 更新失败")
            return False

    def backup(self) -> bool:
        """
        备份模式：从安装目录选择多个配置文件备份到仓库

        Returns:
            是否成功
        """
        print("\n💾 备份模式：安装目录 → 仓库")
        print(f"安装目录: {self.opencode_target}")
        print(f"仓库目录: {self.opencode_repo}\n")

        # 验证路径
        if not self.validate_paths():
            return False

        # 显示选择界面
        src_files = self.show_backup_selector()
        if src_files is None or len(src_files) == 0:
            print("❌ 操作已取消")
            return False

        # 显示差异
        print(f"\n📊 检查 {len(src_files)} 个文件的差异...\n")
        files_to_backup = []

        for src_file in src_files:
            dst_file = self.opencode_repo / src_file.name
            has_diff = self.show_diff(src_file, dst_file)
            if has_diff:
                files_to_backup.append((src_file, dst_file))

        if not files_to_backup:
            print("\n✅ 所有文件都已是最新的，无需备份")
            return True

        # 确认操作
        file_list = "\n".join([f"  - {src.name} → {dst.name}" for src, dst in files_to_backup])
        action_desc = f"备份 {len(files_to_backup)} 个文件到仓库:\n{file_list}"
        if not self.confirm_action(action_desc):
            print("❌ 操作已取消")
            return False

        # 执行备份
        success = True
        print(f"\n📋 正在备份...")
        for src_file, dst_file in files_to_backup:
            if self.sync_file(src_file, dst_file):
                print(f"✅ {src_file.name} 备份成功")
            else:
                print(f"❌ {src_file.name} 备份失败")
                success = False

        if success:
            print(f"\n✅ 所有文件备份成功!")
            print(f"💡 提示: 记得将修改提交到 Git 仓库")
        else:
            print(f"\n❌ 部分文件备份失败")

        return success


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="配置文件同步脚本 - 同步仓库配置文件与实际安装目录",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 更新模式：从仓库选择一个配置文件更新到安装目录
  python script/sync.py update

  # 备份模式：从安装目录选择多个配置文件备份到仓库
  python script/sync.py backup

目录映射:
  opencode/  → ~/.config/opencode
  skills/    → ~/.agents/skills

功能说明:
  - 更新模式: 从仓库选择一个配置文件（单选）更新到 ~/.config/opencode/oh-my-opencode.jsonc
  - 备份模式: 从 ~/.config/opencode 选择多个配置文件（多选）备份到仓库 opencode/ 目录
        """
    )

    parser.add_argument(
        "action",
        choices=["update", "backup"],
        help="操作类型: update(更新), backup(备份)"
    )

    parser.add_argument(
        "--repo-root",
        type=str,
        default=None,
        help="仓库根目录 (默认: 脚本所在目录的父目录)"
    )

    args = parser.parse_args()

    # 确定仓库根目录
    if args.repo_root:
        repo_root = Path(args.repo_root)
    else:
        # 脚本所在目录的父目录
        script_dir = Path(__file__).parent
        repo_root = script_dir.parent

    # 创建同步管理器
    sync = ConfigSync(repo_root)

    # 执行操作
    if args.action == "update":
        success = sync.update()
        sys.exit(0 if success else 1)

    elif args.action == "backup":
        success = sync.backup()
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
