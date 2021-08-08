import re


class Regex():
    def allocate_time(self, name_of_card):
        self.name_of_card = name_of_card
        allocate_time = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',self.name_of_card)
        return allocate_time