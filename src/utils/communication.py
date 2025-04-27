import inquirer

from typing import List, Any

def communicate_with_user(
  type: str = "",
  name: str = "defualt",
  message: str = "Please provide your input",
  defualt: bool = True,
  choices: List[Any] = None,
  carousel: bool = True
) -> Any:
  """Prompts the user for input, confirmation, or selection based on the specified type.""" 
  if choices is None: choices = []
  user_choice: any
  match type:
    case "input":
      user_choice = inquirer.prompt(
        [inquirer.Text(name, message=message)]
      )
    case "confirm":
      user_choice = inquirer.prompt(
        [inquirer.Confirm(name, message=message, default=defualt)]
      )
    case "list":
      user_choice = inquirer.prompt(
        [inquirer.List(name, message=message, choices=[*choices])]
      )
    case "checkbox":
      user_choice = inquirer.prompt(
        [inquirer.Checkbox(name, message=message, choices=[*choices])]
      )
    case "password":
      user_choice = inquirer.prompt(
        [inquirer.Password(name, message=message)]
      )
    case "listJS": # similarly to Node.js by adding carousel
      user_choice = inquirer.prompt(
        [inquirer.List(name, message=message, choices=[*choices], carousel=carousel)]
      )
    case "editor":
      user_choice = inquirer.prompt(
        [inquirer.Editor(name, message=message)]
      )
    case "number":
      user_choice = inquirer.prompt(
        [inquirer.Number(name, message=message)]
      )
    case _: # Default case for unrecognized input type
      user_choice = inquirer.prompt(
        [inquirer.Text("continue", message="Press anything to continue")]
      )
      print()
  return user_choice
