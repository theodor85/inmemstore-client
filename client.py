from typing import Tuple, Optional, Callable


def command():
    return 'OK'


def parse_command(input_command: str) -> Tuple[str, Optional[Callable]]:
    if input_command not in ['set', 'get']:
        return 'Unknown command', None
    return '', command


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
            message = command()
            print(message)


if __name__ == "__main__":
    main()
