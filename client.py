from typing import Tuple, Optional, Callable

from commands import COMMANDS


def parse_command(input_command: str) -> Tuple[str, Optional[Callable]]:

    str_command = input_command.split(' ')[0].strip()

    if str_command not in COMMANDS.keys():
        return 'Unknown command', None
    return '', COMMANDS[str_command]


def head():
    print('-'*50)
    print('** Client for In-memory key-value storage')
    print('** Available commands:')
    print('** exit')
    print('** set key=value key2=value ...')
    print('** get key1 key2 ...')
    print('** del key1 key2 ...')
    print('** list')
    print('** clear')
    print('-'*50)


def main():
    input_command = ''
    head()
    while True:
        input_command = input('>')
        if input_command == 'exit':
            break
        error_message, command = parse_command(input_command)
        if error_message:
            print(error_message)
        else:
            message = command(input_command)
            print(message)


if __name__ == "__main__":
    main()
