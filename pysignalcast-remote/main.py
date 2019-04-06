
# implement imports here


plugins = ["plug.torrent", "plug.magnet", "plug.url"]


def main():
    while True:
        todo = get_commands()
        result = handle_commands(todo)
        print(result)
        break



def get_commands():
    # implement client server
    return None


def handle_commands(args):
    if args == None:
        return 0
    else:
        return True


main()

'''
todo:
implement proper plugin system
implement client server logic
    - implement authentication
implement selenium driver
integrate with jdownloader/some other service
'''
