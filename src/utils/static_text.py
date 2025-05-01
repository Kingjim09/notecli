def show_help() -> None:
  """Display detailed help information about the CLI options and behavior."""
  print("""## Note CLI Help

This CLI tool allows you to interact with files and directories directly from the terminal. Below are the available commands and their usage.

### File and Directory Navigation
- **Select a file**: If a **file** is selected, its contents will be displayed in **read-only** mode, allowing you to view its content but not modify it.
- **Select a directory**: If a **directory** is selected, the CLI will navigate into that directory, displaying its contents, and enabling further navigation.

### Available Commands
- **..**: Go back one directory from your current location.
- **Edit File**: Open an existing file for editing. You can modify its contents directly in the terminal.
- **Create File**: Create a new file in the current directory. Provide a name and optional content for the file.
- **Create Folder**: Create a new folder in the current directory. Provide a name for the folder.
- **Change Default Path**: Change the default working directory for the CLI tool. This will set a new base directory for navigation and file operations.
- **Delete**: Delete a file or folder from the current directory. Be careful, as this operation is irreversible.
- **Help**: Display this detailed help message, which explains the available options and commands.
- **Exit**: Exit the application with a friendly farewell message.

### Additional Information
- **Navigation**: When navigating directories, you can use the `..` command to return to the parent directory.
- **File Management**: Editing files and creating folders or files is straightforward; however, ensure you provide valid paths to avoid errors.

Feel free to explore and use these commands to manage your files and directories effectively!
  """)
