from Machine import Machine


def main():
    regex_for_ip = r'(?:[0-254]){4}'
    machine1 = Machine()
    machine1.print_interface_list()


if __name__ == '__main__':
    main()
