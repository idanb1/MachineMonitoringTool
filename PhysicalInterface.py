from Interface import Interface
from NICOperations import NICOperations

class PhysicalInterface(Interface):

    def __init__(self):
        super(Interface, self).__init__()

    def get_interface_name(self):
        pass

    def get_ip_address(self):
        pass

    def get_mac_address(self):
        pass

    def set_ip_address(self):
        pass
