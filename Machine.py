from NICOperations import NICOperations


class Machine:

    def __init__(self):
        self.interfaces_names_list = NICOperations.set_command('ifconfig | grep ".*: "').split('\n')

    def print_interface_list(self):
        for interface_name in self.interfaces_names_list:
            print(interface_name)
