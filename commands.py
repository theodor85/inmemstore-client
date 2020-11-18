import requests
from requests.exceptions import ConnectionError


COMMANDS = dict()


def register_command(name):
    def decorator(func):
        COMMANDS[name] = func
        return func
    return decorator


@register_command(name='set')
def command_set(user_input: str) -> str:

    HELP_MESSAGE = ''' Argument string must be like this:
        set key1=value1 key2=value2 ...'''

    args = user_input.strip().split(' ')[1:]
    message = ''

    if not args:
        message = 'There are no arguments in "set" command.' + HELP_MESSAGE

    json_for_send = dict()
    for arg in args:
        # validation
        # key=value
        if arg.find('=') == -1:
            message = 'Bad argument format for "set" command.' + HELP_MESSAGE
            break
        key = arg.split('=')[0].strip()
        if not key:
            message = 'Bad argument format for "set" command.' + HELP_MESSAGE
            break
        value = arg.split('=')[1].strip()
        if not value:
            message = 'Bad argument format for "set" command.' + HELP_MESSAGE
            break

        json_for_send[key] = value

    if not message:
        URL = 'http://0.0.0.0:8080/keys'
        try:
            response = requests.post(URL, json=json_for_send)
        except ConnectionError:
            message = 'Connection error while connect to server'
        else:
            if response.status_code != 201:
                message = 'Server error with status code '
                f'{response.status_code}'
            else:
                message = 'Key-value pairs was updated successfully'

    return message


@register_command(name='get')
def command_get():
    return 'get OK'


@register_command(name='del')
def command_del():
    return 'del OK'


@register_command(name='list')
def command_list(user_input: str) -> str:

    message = ''

    URL = 'http://0.0.0.0:8080/keys'
    try:
        response = requests.get(URL)
    except ConnectionError:
        message = 'Connection error while connect to server'
    else:
        if response.status_code != 200:
            message = 'Server error with status code '
            f'{response.status_code}'
        else:
            for key, value in response.json().items():
                message += f'{key}={value} '

    return message


@register_command(name='clear')
def command_clear(user_input: str) -> str:

    message = ''

    URL = 'http://0.0.0.0:8080/keys/clear'
    try:
        response = requests.post(URL)
    except ConnectionError:
        message = 'Connection error while connect to server'
    else:
        if response.status_code != 204:
            message = 'Server error with status code '
            f'{response.status_code}'
        else:
            message = 'Storage was cleaned successfully'

    return message
