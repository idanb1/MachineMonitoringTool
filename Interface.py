class Interface():

    # Generic Object attributes:
    notImplementedAbstractErr = "SubClass needs to implement this abstract mathod"

    def __init__(self):
        self.name = self.get_interface_name()
        self.ip = self.get_ip_address()
        self.mac = self.get_mac_address()

    def get_interface_name(self):
        raise NotImplementedError(Interface.notImplementedAbstractErr)

    def get_ip_address(self):
        raise NotImplementedError(Interface.notImplementedAbstractErr)

    def get_mac_address(self):
        raise NotImplementedError(Interface.notImplementedAbstractErr)

    def set_ip_address(self):
        raise NotImplementedError(Interface.notImplementedAbstractErr)

    def __str__(self):
        pass