import os
import re
import subprocess

class NICOperations:

    @staticmethod
    def set_command(command):
        """

        :param command:
        :return: shell returned output
        """
        return os.popen(command).read()

    @staticmethod
    def get_value_with_given_regex(pattern, input):
        pattern = re.compile(pattern)
        re.search(pattern, input)
