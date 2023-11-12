
class Ciphers:

    def __init__(self, cipher='Alphanumeric Qabbala'):
        self.gematria = {}

        if cipher == 'Alphanumeric Qabbala':
            self.alphanumeric_qabbala()
        elif cipher == 'English Ordinal':
            self.english_ordinal()

    def alphanumeric_qabbala(self):
        for i in range(36):
            if i < 10:
                self.gematria[str(i)] = i
            else:
                self.gematria[chr(65 + i - 10)] = i 
        return self.gematria

    def english_ordinal(self):
        for i in range(26):
            self.gematria[chr(65 + i)] = i + 1
        return self.gematria

