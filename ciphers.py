

aq = {
    0 : 0, 1 : 1, 2 : 2, 3 : 3, 4 : 4,
    5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9,
    'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14,
    'F' : 15, 'G' : 16, 'H' : 17, 'I' : 18, 'J' : 19,
    'K' : 20, 'L' : 21, 'M' : 22, 'N' : 23, 'O' : 24,
    'P' : 25, 'Q' : 26, 'R' : 27, 'S' : 28, 'T' : 29,
    'U' : 30, 'V' : 31, 'W' : 32, 'X' : 33, 'Y' : 34,
    'Z' : 35
}

english_ordinal = {
    1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5,
    6 : 6, 7 : 7, 8 : 8, 9 : 9, 
    'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
    'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
    'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
    'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
    'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25,
    'Z' : 26

}

# ... more ciphers

class Ciphers:

    def __init__(self):
        self.gematria = {}

    def alphanumeric_qabbala(self):
        for i in range(36):
            if i < 10:
                self.gematria[i] = i
            else:
                self.gematria[chr(65 + i - 10)] = i
        return self.gematria
    
    def english_ordinal(self):
        for i in range(26):
            self.gematria[chr(65 + i)] = i + 1
        return self.gematria