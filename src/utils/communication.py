import inquirer
from typing import Any, List

def prompt_user_for_input(
  prompt_type: str = "",
  field_name: str = "default",
  prompt_message: str = "Please provide your input",
  default_answer: bool = True,
  available_choices: List[Any] = None,
  enable_carousel: bool = True
) -> Any:
  """Prompts the user for input, confirmation, or selection based on the specified prompt type."""
  if available_choices is None:
    available_choices = []
  
  user_response: Any

  match prompt_type:
    case "input":
      user_response = inquirer.prompt([
        inquirer.Text(field_name, message=prompt_message)
      ])
    case "confirm":
      user_response = inquirer.prompt([
        inquirer.Confirm(field_name, message=prompt_message, default=default_answer)
      ])
    case "list":
      user_response = inquirer.prompt([
        inquirer.List(field_name, message=prompt_message, choices=available_choices)
      ])
    case "checkbox":
      user_response = inquirer.prompt([
        inquirer.Checkbox(field_name, message=prompt_message, choices=available_choices)
      ])
    case "password":
      user_response = inquirer.prompt([
        inquirer.Password(field_name, message=prompt_message)
      ])
    case "listJS":  # Adds carousel functionality, similar to Node.js
      user_response = inquirer.prompt([
        inquirer.List(field_name, message=prompt_message, choices=available_choices, carousel=enable_carousel)
      ])
    case "editor":
      user_response = inquirer.prompt([
        inquirer.Editor(field_name, message=prompt_message)
      ])
    case "number":
      user_response = inquirer.prompt([
        inquirer.Number(field_name, message=prompt_message)
      ])
    case _:
      user_response = inquirer.prompt([
        inquirer.Text(field_name, message="Press enter to continue")
      ])
      print()  
  return user_response
