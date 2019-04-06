
# implement imports here


plugins = ["plug.torrent", "plug.magnet", "plug.url"]


def main():
    while True:
        todo = get_commands()
        result = handle_commands(todo)
        print(result)
        break



def get_commands():
    return None



def dosomething():
    return True



def handle_commands(args):
    if args == None:
        return 0
    else:
        return True


main()