from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from rich import print as rprint

from os.path import isfile


from datetime import date




from file_utils import read_file



def prompt_license() -> str:
    result = LICENSE_PROMPT.execute()

    if result == "cc":
        return prompt_cc()
    
    return result


def prompt_cc():
    while True:
        #TODO: Tidy this up to only create the select once

        selection = CC_LICENSE_PROMPT.execute()

        if selection == "info":
            rprint(CC_INFO_TEXT)
        else:
            return selection


def generate_license_text(license, project_name, author):
    information: dict[str, str] = {
        "%YEAR%": str(date.today().year),
        "%PROJECT%": project_name,
        "%AUTHOR%": author,
    }

    if license.startswith("cc-"):
        information["%CC_TYPE%"] = license.removeprefix("cc-")
        information["%CC_TYPE_UPPER%"] = information["%CC_TYPE%"].upper()
        license = "cc"  # Change license name for file reading
    
    license_text: str | None = read_file(f"./license_notices/{license}.txt")

    if not license_text:
        license_text = f"This project is licensed under {license.upper()}"


    for key, value in information.items():
        license_text = license_text.replace(key, value)
    
    return license_text




# =================
#     CONSTANTS
# =================

LICENSE_PROMPT = inquirer.select(
    message="Choose a license type:",
    choices=[
        Choice("mit", "MIT License"),
        Choice("apache-2", "Apache License 2.0"),
        Choice("gpl-3", "GNU General Public License (GPL v3)"),
        Choice("lgpl-3", "GNU Lesser General Public License (LGPL v3)"),
        Choice("mpl-2", "Mozilla Public License 2.0 (MPL 2.0)"),
        Choice("cc", "Creative Commons Licenses (CC0, CC BY, etc.)"),
        Choice("unlicense", "Unlicense"),
        ],
)

# Predefining the CC license prompt to avoid recreating this object every time
# the user wants to get more information about the license types.
CC_LICENSE_PROMPT = inquirer.select(
    message="Choose a Creative Commons license:",
    choices=[
        Choice("info", "Explain the options"),
        Separator(),
        Choice("cc0", "No Rights Reserved (CC0)"),
        Choice("cc-by", "Attribution (CC BY)"),
        Choice("cc-by-sa", "Attribution-ShareAlike (CC BY-SA)"),
        Choice("cc-by-nc", "Attribution-NonCommercial (CC BY-NC)"),
        Choice("cc-by-nc-sa", "Attribution-NonCommercial-ShareAlike (CC BY-NC-SA)"),
        Choice("cc-by-nd", "Attribution-NoDerivatives (CC BY-ND)"),
        Choice("cc-by-nc-nd", "Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND)"),
        ],
)

CC_INFO_TEXT = """
[bold red]CC0[/bold red]\tThe work has been marked as dedicated to the public domain.
[bold red]BY[/bold red]\tCredit must be given to the creator.
[bold red]SA[/bold red]\tAdaptations must be shared under the same terms.
[bold red]ND[/bold red]\tNo derivatives or adaptations of the work are permitted.

More information at <https://creativecommons.org/share-your-work/cclicenses/>

"""