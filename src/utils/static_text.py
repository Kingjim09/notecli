def show_help() -> None:
  """Display help information about the CLI options and behavior."""
  print("""## Help

When you select a file or directory, the CLI automatically detects its type.  
- If a **file** is selected, its contents are displayed in **read-only** mode.  
- If a **directory** is selected, the CLI navigates into that directory, allowing you to view its contents.

### Default Options Explained

- **..**: Go back one directory from the current location.
- **Edit File**: Open and edit an existing file directly within the terminal.
- **Create File**: Create a new file in the current working directory.
- **Create Folder**: Create a new folder in the current working directory.
- **Change Default Path**: Update the default working directory for the Note CLI.
- **Delete**: Remove a file or folder from the current working directory.
- **Help**: View detailed information about available options and usage.
- **Exit**: Close the application with a farewell message.
  """)
