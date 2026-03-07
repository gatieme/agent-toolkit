# Scripts

This directory contains utility scripts for managing the agent-toolkit repository.

## Available Scripts

### sync.py - Configuration File Synchronization

Interactive configuration file synchronization script with TUI interface for bidirectional synchronization between the repository and actual installation directories.

#### Features

- **Update Mode**: Select a single configuration file from the repository and update it to the installation directory
- **Backup Mode**: Select multiple configuration files from the installation directory and backup them to the repository
- **TUI Interface**: Modern terminal UI using `prompt_toolkit` with Tab navigation
- **Diff Preview**: Show differences before synchronization operations
- **Confirmation Prompts**: Safety confirmation before making changes
- **Smart Filtering**: Automatically discovers and filters `oh-my-opencode-*.jsonc` configuration files

#### Directory Mapping

| Repository Directory | Installation Directory |
|:---------------------|:-----------------------|
| `opencode/`          | `~/.config/opencode`   |
| `skills/`            | `~/.agents/skills`     |

#### Dependencies

```bash
pip3 install prompt_toolkit --user
```

#### Usage

##### Update Mode (Repository → Installation)

Update a single configuration file from the repository to the installation directory:

```bash
python script/sync.py update
```

**Workflow:**
1. Select a configuration file from `opencode/` directory (single selection)
    - Options include: `oh-my-opencode.jsonc`, `oh-my-opencode-interactive.jsonc`, `oh-my-opencode-ultraworker.jsonc`, etc.
2. Review the diff preview showing changes
3. Confirm the operation
4. The selected file is copied to `~/.config/opencode/oh-my-opencode.jsonc`

##### Backup Mode (Installation → Repository)

Backup multiple configuration files from the installation directory to the repository:

```bash
python script/sync.py backup
```

**Workflow:**
1. Select configuration files from `~/.config/opencode` (multiple selection)
    - Options include all `oh-my-opencode-*.jsonc` files in the installation directory
2. Review the diff preview for each selected file
3. Confirm the operation
4. Selected files are copied to the repository `opencode/` directory

##### Help

Display help information:

```bash
python script/sync.py --help
```

#### Examples

```bash
# Update oh-my-opencode-interactive.jsonc from repo to installation
python script/sync.py update
# → Select "oh-my-opencode-interactive.jsonc"
# → Review diff
# → Confirm
# → File copied to ~/.config/opencode/oh-my-opencode.jsonc

# Backup multiple configs from installation to repo
python script/sync.py backup
# → Select "oh-my-opencode.jsonc" and "oh-my-opencode-ULTRAWORKER.jsonc"
# → Review diffs
# → Confirm
# → Files copied to opencode/ directory
```

#### How It Works

1. **File Discovery**: The script automatically discovers configuration files matching the patterns:
   - `oh-my-opencode.jsonc`
   - `oh-my-opencode-*.jsonc`
   - `oh-my-opencode-slim.json`

2. **TUI Selection**: Uses `prompt_toolkit` dialogs for user interaction:
   - `radiolist_dialog` for single selection (update mode)
   - `checkboxlist_dialog` for multiple selection (backup mode)

3. **Diff Comparison**: Uses the system `diff` command to show differences:
   - Shows unified diff format
   - Limits output to 100100 lines for readability
   - Falls back to simple comparison if `diff` is unavailable

4. **Safe Operations**: 
   - Always shows diff before making changes
   - Requires explicit confirmation
   - Creates target directories if needed
   - Preserves file metadata (using `shutil.copy2`)

#### Safety Features

- **Diff Preview**: Always shows what will change before executing
- **Confirmation Required**: Must explicitly confirm each operation
- **No Overwrite Without Warning**: Clear indication of what will be overwritten
- **Error Handling**: Comprehensive error messages and graceful handling
- **Path Validation**: Checks that source and target directories exist

#### Error Handling

The script handles various error scenarios:

- Missing source or target directories
- No configuration files found
- File permission issues
- `diff` command not available (falls back to simple comparison)
- User cancellation at any step

#### Tips

1. **Commit After Backup**: After using backup mode, remember to commit the changes to Git:
   ```bash
   git add opencode/
   git commit -m "backup: update configuration files from installation"
   ```

2. **Check Installation Directory**: Ensure `~/.config/opencode` exists before running the script

3. **Review Diff Carefully**: Always review the diff output to understand what will change

4. **Use Relative Paths**: The script automatically determines the repository root based on its location

#### Technical Details

- **Python Version**: Requires Python 3.6+
- **Platform**: Cross-platform (Linux, macOS, Windows)
- **Terminal**: Requires terminal with UTF-8 support for proper display
- **File Encoding**: UTF-8 for all configuration files

## Contributing

When adding new scripts to this directory:

1. Add appropriate documentation to this README
2. Include usage examples
3. List dependencies clearly
4. Follow the existing code style
5. Add error handling and user-friendly messages
6. Consider adding help text to the script

## License

Same as the parent agent-toolkit repository.
