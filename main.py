import openai  # pip install openai
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table
import config

"""
Useful websites:
- OpenAI module: https://github.com/openai/openai-python
- ChatGPT API documentation: https://platform.openai.com/docs/api-reference/chat
- Typer: https://typer.tiangolo.com
- Rich: https://rich.readthedocs.io/en/stable/
"""


def main():

    openai.api_key = config.api_key

    print("💬 [bold green]ChatGPT API in Python[/bold green]")

    table = Table("Command", "Description")
    table.add_row("exit", "Exit the application")
    table.add_row("new", "Create a new conversation")

    print(table)

    # Assistant context
    context = {"role": "system",
               "content": "You are a very useful assistant."}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("🆕 New conversation created")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\nWhat do you want to talk about? ")

    if prompt == "exit":
        exit = typer.confirm("✋ Are you sure?")
        if exit:
            print("👋 Goodbye!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)

