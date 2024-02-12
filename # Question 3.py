# Question 3 do not understand not allowed to print the whole pattern so I have done it end to end

class Pattern:
    def __init__(self, size):
        self.size = size

    def multiple(self, char1, char2):
        for i in range(1, self.size + 1):
            if i % 2 != 0:
                print(char1 * i)
            else:
                print(char2 * i)


pattern = Pattern(5)  
pattern.multiple('@','@')

class Pattern:
    def __init__(self, size):
        self.size = size

    def multiple(self, char1, char2):
        for i in range(self.size, 0, -1):  # Loop in reverse order
            if i % 2 != 0:
                print(char1 * i)
            else:
                print(char2 * i)


pattern = Pattern(5)
pattern.multiple('#', '#')


class Pattern:
    def __init__(self, size):
        self.size = size

    def multiple(self, char1, char2):
        for i in range(1, self.size + 1):
            if i % 2 != 0:
                print(char1 * i)
            else:
                print(char2 * i)


pattern = Pattern(5) 
pattern.multiple('*','*')

class Pattern:
    def __init__(self, size):
        self.size = size

    def multiple(self, char1, char2):
        for i in range(self.size, 0, -1):  # Loop in reverse order
            if i % 2 != 0:
                print(char1 * i)
            else:
                print(char2 * i)


pattern = Pattern(5)
pattern.multiple('%', '%')
