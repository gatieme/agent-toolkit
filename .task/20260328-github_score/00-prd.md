/superpowers:brainstorm plugin/README 中列出了很多 Claude Code, OpenCode 相关的插件和工具，以 Markdown 形式组织，现在要求对每个项目进行推荐星级和Star 数量的更新。
在 script 实现一套 python 脚本，对输入的指定 github 地址，获取其相关信息并评分。最后更新  plugin/README
1. 当前已经存在的 script/get_github_stars.py 比如 obra/superpowers，可以获取 github 仓库的相关信息。请继续更新此脚本，设计一套评分规则，可以通过通过 Stars 数量，Forks，Watchers，Issues 等各种信息对此项目评分，5 星 最高，1 星最低。
2. 生成一个新的 python 脚本，调用 script/get_github_stars.py 的 API，更新 plugin/README，更新 MARKDOWN 表格中各项目评级以及 Star 数量字段
