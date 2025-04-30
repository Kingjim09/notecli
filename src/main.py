import sys
import time
from typing import Any, List
from utils.communication import communicate_with_user
from utils.file_utils import (
  check_if_file_or_dir,
  change_path,
  clear_terminal,
  delete_file_or_dir,
  get_os,
  get_path,
  go_back,
  text_animation
)
from utils.static_text import show_help

entries: List[str] = get_path(get_os())
default_option: List[str] = [
  "Edit File",
  "Create File",
  "Create Folder",
  "Change Default Path",
  "Delete",
  "Help",
  "Exit"
]

current_path: str = get_os()

def main() -> None:
  """Handles the main logic for user interaction and action selection."""
  global entries, current_path
  userChoice: Any = communicate_with_user("list", "option", "What would you like to do?", choices=choices)
  try:
    if userChoice:
      choice: str = userChoice["option"]
      match choice:
        case "..":
          new_path, entries = go_back(current_path)
          current_path = new_path
        case "Edit File":
          print(f"User has selected '{choice}'.\n")
        case "Create File":
          print(f"User has selected '{choice}'.\n")
        case "Create Folder":
          print(f"User has selected '{choice}'.\n")
        case "Change Default Path":
          new_path: str = input("Enter the new path: ").strip()
          entries = change_path(new_path)
        case "Delete":
          clear_terminal()
          deleted_choice: Any = communicate_with_user("list", "option", "What would you like to delete?", choices=[*entries, "Exit"])
          choice: str = deleted_choice["option"]
          if choice == "Exit": 
            text_animation(message="Going back...")
            print()
          else: delete_file_or_dir(choice)
        case "Help": 
          clear_terminal()
          show_help()
          input("Press Enter to return...")
          clear_terminal()
        case "Exit":
          text_animation(message="Thank you for using the Note CLI. Goodbye!...") 
          time.sleep(0.5)
          clear_terminal()
          sys.exit(0)
        case _:
          check_user_choice: str | None = check_if_file_or_dir(choice)
          match check_user_choice:
            case "File":
              print(f"'{choice}' is a File.\n")
            case "Dir":
              print(f"'{choice}' is a Directory.\n")
            case None:
              print(f"'{choice}' is neither a File or Directory.\n")
          input("Press Enter to continue...")
    else:
      raise Exception("Something happened when selecting your choice.")
  except Exception as e:
    print(f"Unexpected Error: {e}")

if __name__ == "__main__":
  clear_terminal()
  print("=== Welcome to Note CLI ===\n")
  while True:
    choices: List[str] = ["..", *entries, *default_option]
    main()
    # Clear the terminal after each main() loop iteration to keep the interface clean
    clear_terminal()

