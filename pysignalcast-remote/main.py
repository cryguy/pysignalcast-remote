
# implement imports here


# TODO: implement proper plugin system
plugins = ["plug.torrent", "plug.magnet", "plug.url"]


def main():
    while True:
        # TODO: implement selenium driver
        # TODO: integrate with jdownloader/some other service
        todo = get_commands()
        result = handle_commands(todo)
        print(result)
        break


# TODO: implement client server logic
def get_commands():
    return None


def handle_commands(args):
    if args == None:
        return 0
    else:
        return True


main()

