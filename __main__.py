from markdown import MarkdownDocument

from InquirerPy import inquirer
from InquirerPy.base.control import Choice


from rich import print as rprint

from license_generator import prompt_license, generate_license_text
from inquirer_utils import prompt_text, prompt_multiline, prompt_yesno


rprint(
    "[bold red]Welcome to the README generator[/bold red]",
    "\t[#8282ae]Version 1.0.0[/#8282ae]",
    "",
    "This application will guide you through the creation of a simple",
    "markdown readme file for your project.",
    sep="\n",
    end="\n\n"
    )


md_doc = MarkdownDocument()

project_name = title = prompt_text("Enter the project name:")


if prompt_yesno("Would you like to give the README a title that is not the project name?", False):
    title = prompt_text("Enter the title of this file:")

sections = ["desc", "install", "usage", "license", "contact"]

if prompt_yesno("Would you customise which sections to include?", False):
    sections = inquirer.select(
            message="Toggle sections with <SPACE> and confirm with <ENTER>:",
            choices=[
                Choice("desc", "Project Description", True),
                Choice("install", "Installation Instructions", True),
                Choice("usage", "Usage Instructions", True),
                Choice("license", "License Selection", True),
                Choice("contact", "Contact / Author Information", True),
            ],
            multiselect=True,
        ).execute()


md_doc.set_title(title)



if "desc" in sections:
    project_description = prompt_multiline("Describe the project:", True)
    md_doc.add_section("Description", project_description)

if "install" in sections:
    project_installation = prompt_multiline("Describe the installation process:", True)
    md_doc.add_section("Installation Instructions", project_installation)

if "usage" in sections:
    project_usage = prompt_multiline("Describe how to run and use the project:", True)
    md_doc.add_section("Usage Guide", project_usage)

if "license" in sections:
    project_license = prompt_license()
    license_author = prompt_text("Enter the author's name (for license purposes):")
    md_doc.add_section("License", generate_license_text(project_license, project_name, license_author))

if "usage" in sections:
    author_contact = prompt_multiline("Detail any contact information:", True)
    md_doc.add_section("Author Contact", author_contact)



with open("README.md", "w+") as file:
    file.write(str(md_doc))