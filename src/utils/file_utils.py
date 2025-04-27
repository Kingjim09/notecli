import json
import sys
import time
import getpass
import platform
import os

from pathlib import Path
from typing import List, Any, Dict

data_file: str = "./data/data.json"

def get_os() -> str:
  """Return the default Documents path based on the user's OS."""
  user: str = getpass.getuser()
  os_name: str = platform.system()

  # Ensure the parent folder for the data file exists
  Path(data_file).parent.mkdir(parents=True, exist_ok=True)

  # Load existing data or initialize an empty dictionary
  if Path(data_file).exists():
    with open(data_file, "r") as f:
      try:
        data: Dict[str, str] = json.load(f)
      except json.JSONDecodeError:
        data = {}
  else:
    data = {}

  if not isinstance(data, dict):
    data = {}

  # Save the current user into the config
  data["user"] = user
  with open(data_file, "w") as f:
    json.dump(data, f)

  # Return the default Documents path based on the OS
  match os_name:
    case "Windows":
      return f"C:\\Users\\{user}\\OneDrive\\Documents"
    case "Linux":
      return f"/home/{user}/OneDrive/Documents"
    case "Darwin":  # Darwin == macOS
      return f"/Users/{user}/OneDrive/Documents"
    case _:
      return "."

def get_path(default_path: str) -> List[str]:
  """Return the list of entries from the stored or newly provided path."""
  try:
    with open(data_file, "r") as f:
      config: Any = json.load(f)
      path: Any = config.get(default_path)
  except (FileNotFoundError, json.JSONDecodeError):
    path = None
    config = {}

  # Prompt user for path if not found
  if not path:
    path = input("Enter the path: ").strip()
    if not path:
      path = default_path
    config[default_path] = path
    with open(data_file, "w") as f:
      json.dump(config, f)

  folder: Path = Path(path)
  entries: List[str] = []

  # Populate entries if folder exists
  if folder.exists() and folder.is_dir():
    entries = [e.name for e in folder.iterdir()]
  else:
    print("Path does not exist or is not a directory.")

  return entries

def change_path(new_path: str, defualt_path: str = get_os()) -> List[str]:
  """Allows the user to change the default path."""
  with open(data_file, "r") as f:
    data = json.load(f)
  if defualt_path in data:
    data[defualt_path] = new_path
  with open(data_file, "w") as f:
    json.dump(data, f)
  folder: Path = Path(new_path)
  entries: List[str] = []
  if folder.exists() and folder.is_dir():
    entries = [e.name for e in folder.iterdir()]
  else:
    print("Path does not exist or is not a directory.")
  return entries

def check_if_file_or_dir(user_choice: str, defualt_path: str = get_os()) -> str | None:
  """Check if the user's choice is a file or directory in the specified path."""
  current_path: Path = Path(defualt_path)
  user_path: Path = current_path / user_choice

  if user_path.exists():
    if user_path.is_file(): return "File"
    elif user_path.is_dir(): return "Dir"
  return None

def exitApp(message: str = "Exiting the App. Goodbye...") -> None:
  """Displays an animated exit message before quitting the application."""
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
  print()
  sys.exit(0)

def clear_terminal() -> None:
  """Clears the terminal."""
  os.system('cls' if os.name == 'nt' else 'clear')
