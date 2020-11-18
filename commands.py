COMMANDS = dict()


def register_command(name):
    def decorator(func):
        COMMANDS[name] = func
        return func
    return decorator


@register_command(name='set')
def command_set():
    return 'set OK'


@register_command(name='get')
def command_get():
    return 'get OK'


@register_command(name='del')
def command_del():
    return 'del OK'


@register_command(name='list')
def command_list():
    return 'list OK'


@register_command(name='clear')
def command_clear():
    return 'clear OK'
