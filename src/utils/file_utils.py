import getpass
import json
import os
import platform
import shutil
import sys
import time
from typing import Any, Dict, List
from pathlib import Path

data_file: str = "./src/data/data.json"

def get_os() -> str:
  """Return the default Documents path based on the user's OS."""
  user: str = getpass.getuser() # Gets the user's username
  os_name: str = platform.system() # Gets the user's OS

  # Ensure the parent folder for the data file exists
  Path(data_file).parent.mkdir(parents=True, exist_ok=True)

  # Load existing data or initialize an empty dictionary
  if Path(data_file).exists():
    with open(data_file, "r") as f:
      try: data: Dict[str, str] = json.load(f)
      except json.JSONDecodeError: data = {}
  else: data = {}

  if not isinstance(data, dict): data = {}

  # Save the current user into the config
  data["user"] = user
  with open(data_file, "w") as f: json.dump(data, f)

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
    if not path: path = default_path
    config[default_path] = path
    with open(data_file, "w") as f: json.dump(config, f)

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
  with open(data_file, "r") as f: data = json.load(f)

  if defualt_path in data: data[defualt_path] = new_path

  with open(data_file, "w") as f: json.dump(data, f)

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

def delete_file_or_dir(delete_path: str, default_path: str = get_os()) -> None:
  """Deletes a file or directory at the given path relative to the default OS path."""
  current_path: Path = Path(default_path)
  deletion_path: Path = current_path / delete_path
  check_delete_path: str = ""

  if not deletion_path.exists():
    print("The path doesn't exist.")
  
  if deletion_path.is_file(): check_delete_path = "File"
  elif deletion_path.is_dir(): check_delete_path = "Dir"

  match check_delete_path:
    case "File":
      os.remove(deletion_path)
      print("Successfully deleted the file.")
    case "Dir":
      shutil.rmtree(deletion_path)
      print("Successfully deleted the directory.")
    case _:
      print("Test")
    
def text_animation(delay: int = 0.05, message: str = "") -> None:
  """Animates text output with a delay, showing an error if no message is provided."""
  def animate_text(delay: int = delay, message: str = message) -> None:
    """Prints text character by character with a specified delay."""
    for char in message:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(delay)
    print()
  
  if not message:
    animate_text(message="Please provide a message for the text animation.")
    time.sleep(0.5)
  else: animate_text(delay, message)

def clear_terminal() -> None:
  """Clears the terminal."""
  os.system('cls' if os.name == 'nt' else 'clear')
