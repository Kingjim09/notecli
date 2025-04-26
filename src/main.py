import inquirer, sys, time
from typing import List

choices: list[str] = [
  "Create a File",
  "Create a Folder",
  "Delete",
  "Exit"
]

askQuestion: list[List] = [
  inquirer.List(
    "option",
    message="What would you like to do?",
    choices=[*choices]
  )
]

def exitApp(MESSAGE: str) -> str:
  """Displays an animated exit message before quitting the application."""
  for char in MESSAGE:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
  print()
  sys.exit(0)

def main() -> None:
  """Handles the main logic for user interaction and action selection."""
  userChoice: dict | None = inquirer.prompt(askQuestion)
  try:
    if userChoice:
      choice: str = userChoice["option"]
      match choice:
        case "Create a File":
          print(f"User has selected '{choice}'.")
        case "Create a Folder":
          print(f"User has selected '{choice}'.")
        case "Delete":
          print(f"User has selected '{choice}'.")
        case "Exit":
          exitApp("Thank you for using the Note CLI. Goodbye!...")
    else:
      raise Exception("Something happened when selecting your choice.")
  except Exception as e:
    print(f"Unexpected Error: {e}")

if __name__ == "__main__":
  print("=== Welcome to Note CLI ===")
  while True:
    main()
