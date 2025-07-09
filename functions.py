FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return to-do items.
    :param filepath: the name of a file to be read
    :return: a list of written values
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_todos))

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write to do items in the text file.
    :param todos_arg: a list of todo items
    :param filepath: the name of the file
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# print(__name__)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
