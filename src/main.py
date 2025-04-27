from typing import List, Any
from utils.communication import communicate_with_user
from utils.file_utils import get_os, get_path, change_path, check_if_file_or_dir, exitApp, clear_terminal

entries: List[str] = get_path(get_os())
defualt_option: List[str] = [
  "Edit File"
  "Create File",
  "Create Folder",
  "Change Defualt Path",
  "Delete",
  "Help",
  "Exit"
]

def help() -> None:
  """Display help information about the CLI options and behavior."""
  print("""## Help

When you select a file or directory, the CLI automatically detects its type.  
If a **file** is selected, its contents will be displayed in **read-only** mode.  
If a **directory** is selected, the CLI will navigate into that directory.

### What Each Default Option Does

- **Edit File**: Edit an existing file directly within the terminal.
- **Create a File**: Create a new file in the current working directory.
- **Create a Folder**: Create a new folder in the current working directory.
- **Change Default Path**: Set a new default working directory for the Note CLI.
- **Delete**: Delete a file or folder from the current working directory.
- **Help**: Display information about the available options.
- **Exit**: Exit the application with a farewell message.
""")

def main() -> None:
  """Handles the main logic for user interaction and action selection."""
  userChoice: Any = communicate_with_user("list", "option", "What would you like to do?", choices=[*choices])
  try:    
    if userChoice:
      choice: str = userChoice["option"]
      match choice:
        case "Edit File":
          print(f"User has selected '{choice}'.\n")
        case "Create File":
          print(f"User has selected '{choice}'.\n")
        case "Create Folder":
          print(f"User has selected '{choice}'.\n")
        case "Change Defualt Path":
          new_path: str = input("Enter the new path: ").strip()
          global entries
          entries = change_path(new_path)
        case "Delete":
          print(f"User has selected '{choice}'.\n")
        case "Help": 
          help()
          communicate_with_user()
        case "Exit":
          exitApp("Thank you for using the Note CLI. Goodbye!...")
        case _:
          check_user_choice: str | None = check_if_file_or_dir(choice)
          match check_user_choice:
            case "File":
              print(f"'{choice}' is a File.\n")
            case "Dir":
              print(f"'{choice}' is a Directory.\n")
            case None:
              print(f"'{choice}' is neither a File or Directory.\n")
          communicate_with_user()
    else:
      raise Exception("Something happened when selecting your choice.")
  except Exception as e:
    print(f"Unexpected Error: {e}")

if __name__ == "__main__":
  print("=== Welcome to Note CLI ===\n")
  while True:
    choices: list[str] = [*entries, *defualt_option]
    main()
    # Clear the terminal after each main() loop iteration to keep the interface clean
    clear_terminal()
