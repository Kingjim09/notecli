import textwrap

import os
import textwrap

def display_welcome_banner(width: int = 80, color: str = "\033[92m") -> None:
  """Display the welcome banner for the NoteCLI tool, including additional information about its usage."""
  banner = textwrap.dedent("""\
        _   _       _          _____ _      _____ 
      | \ | |     | |        / ____| |    |_   _|
      |  \| | ___ | |_ ___  | |    | |      | |  
      | . ` |/ _ \| __/ _ \ | |    | |      | |  
      | |\  | (_) | ||  __/ | |____| |____ _| |_ 
      |_| \_|\___/ \__\___|  \_____|______|_____|
      
  Welcome to NoteCLI, a command-line interface note-taking tool.

  Features:
  - Create, view, and edit notes right from your terminal.
  - Easy file management for organizing your notes.
  - Supports both plain text files and password-protected encrypted notes.
  
  Commands:
  - "Edit File": Open and edit existing files.
  - "Create File": Create new note files.
  - "Create Folder": Organize notes by creating folders.
  - "Delete": Remove files or folders.
  - "Change Default Path": Change the directory path for your notes.
  - "Help": Get more information about the tool and its commands.
  - "Exit": Exit the NoteCLI tool.
  
  To get started, choose one of the options from the menu below.
  """)

  terminal_width: int = min(width, os.get_terminal_size().columns)  # Use terminal width or provided width
  print(color + banner.center(terminal_width) + "\033[0m")

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
