import os
import re


class NICOperations:

    @staticmethod
    def set_command(command):
        """

        :param command:
        :return: shell returned output
        """
        os.system(command)
        return os.popen(command).read()

    @staticmethod
    def get_value_with_given_regex(pattern, input):
        pattern = re.compile(pattern)
        re.search(pattern, input)
