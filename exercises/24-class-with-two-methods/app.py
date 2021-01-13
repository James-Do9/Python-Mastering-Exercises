class some_class:
    def __init__(self):
        self.string1 = ""

    def get_String(self):
        self.string1 = input()

    def print_String(self):
        print(self.string1.upper())

str1 = some_class()
str1.get_String()
str1.print_String()