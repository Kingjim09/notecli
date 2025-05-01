import sys
import time
from typing import Any, List, Dict
from pathlib import Path
from utils.communication import communicate_with_user
from utils.file_utils import (
  check_if_file_or_dir,
  change_path,
  create_file,
  create_folder,
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
  user_choice: Dict[str, Any] = communicate_with_user("list", "option", "What would you like to do?", choices=choices)
  
  try:
    if user_choice:
      selected_option: str = user_choice["option"]
      match selected_option:
        case "..":
          new_path: str
          new_path, entries = go_back(current_path)
          current_path = new_path
        case "Edit File":
          print(f"User has selected '{selected_option}'.\n")
        case "Create File":
          while True:
            new_file_name_input: Dict[str, str] = communicate_with_user("input", "new file", "What will be the name of the new file?")
            current_path = Path(current_path)
            new_file_path: Path = current_path / new_file_name_input["new file"]

            if new_file_path.name.strip() != "":
              should_include_content: Dict[str, bool] = communicate_with_user("confirm", "include file content", "Do you want to add content to the file?", True)
              if should_include_content["include file content"]:
                new_file_content: Dict[str, str] = communicate_with_user("input", "file content", f"What would be the file content for {new_file_path}?")
                create_file(new_file_path, new_file_content["file content"])
              else:
                create_file(new_file_path)

              entries = get_path(str(current_path))
              break
            else:
              text_animation("Please enter a valid file name.")
        case "Create Folder":
          while True:
            new_folder_name_input: Dict[str, str] = communicate_with_user("input", "folder name", "What will be the name of the new folder?")
            new_folder_name: str = new_folder_name_input["folder name"].strip()
            if new_folder_name != "":
              current_path = Path(current_path)
              folder_path: Path = current_path / new_folder_name
              create_folder(folder_path)
              break
            else:
              text_animation("Please enter a valid folder name.")
          entries = get_path(str(current_path))
        case "Change Default Path":
          new_path: str = input("Enter the new path: ").strip()
          entries = change_path(new_path)
        case "Delete":
          clear_terminal()
          delete_choice: Dict[str, str] = communicate_with_user("list", "option", "What would you like to delete?", choices=[*entries, "Exit"])
          if delete_choice["option"] == "Exit":
            text_animation(message="Going back...")
            print()
          else:
            delete_file_or_dir(delete_choice["option"])
            entries = get_path(str(current_path))
        case "Help":
          clear_terminal()
          show_help()
          communicate_with_user()
          clear_terminal()
        case "Exit":
          text_animation(message="Thank you for using the Note CLI. Goodbye!...") 
          time.sleep(0.5)
          clear_terminal()
          sys.exit(0)
        case _:
          check_user_choice: str | None = check_if_file_or_dir(selected_option)
          match check_user_choice:
            case "File":
              print(f"'{selected_option}' is a File.\n")
            case "Dir":
              print(f"'{selected_option}' is a Directory.\n")
            case None:
              print(f"'{selected_option}' is neither a File or Directory.\n")
          communicate_with_user()
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
