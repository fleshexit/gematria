class AlphanumericQabbala:

    def __init__(self):
        self.gematria = {}
        self.create_gematria()

    def create_gematria(self):
        for i in range(36):
            if i < 10:
                self.gematria[str(i)] = i
            else:
                self.gematria[chr(65 + i - 10)] = i 
        return self.gematria

    def calculate(self, user_input):
        user_input = user_input.upper()
        value = 0
        for char in user_input: # iterate through string
            if char in self.gematria: # check if char is in dict
                value += self.gematria[char] # add value to total

        return value

class EnglishOrdinal:

    def __init__(self):
        self.gematria = {}
        self.create_gematria()

    def create_gematria(self):
        for i in range(26):
            self.gematria[chr(65 + i)] = i + 1
        return self.gematria

    def calculate(self, user_input):
        user_input = user_input.upper()
        value = 0
        for char in user_input:
            if char in self.gematria:
                value += self.gematria[char]
                
        return value