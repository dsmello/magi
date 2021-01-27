import click
from magi.execution import run



@click.command()
@click.option('-d', '--dir', 'directory', required=True, help='The directory of yaml file to do deploy.')
# @click.option('-f', '--file', 'file', required=False, help='The yaml file name (file.: input.yaml || use .: input ) to do deploy.')
def command(directory: str = ""):
    run(folder_path=directory)


if __name__ == '__main__':
    command()
