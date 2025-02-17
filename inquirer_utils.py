from InquirerPy import inquirer


def prompt_text(message: str, allow_empty: bool=False) -> str:
    return inquirer.text(
            message=message,
            validate=lambda x: allow_empty or x.strip()
        ).execute().strip()

def prompt_multiline(message: str, allow_empty: bool=False) -> str:
    return inquirer.text(
            message=message,
            validate=lambda x: allow_empty or x.strip(),
            multiline=True
        ).execute().strip()

def prompt_yesno(message: str, default: bool= True):
    return inquirer.confirm(
            message=message,
            default=default
        ).execute()