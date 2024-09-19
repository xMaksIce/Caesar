class Caesar:
    def __init__(self):
        pass

    def _crypt(self, text, key, decrypt=False):
        crypt = lambda x, y: x + y
        if decrypt:
            crypt = lambda x, y: x - y
        open_text = text.replace("ё", "е").replace("Ё", "Е")
        close_chars = []
        for char in open_text:
            num = ord(char)-1040
            if num >= 0 and num <= 62:
                crypt_num = (crypt(num, key)) % 32
                if num >= 32:
                    crypt_num += 32
                crypt_num += 1040
                crypt_char = chr(crypt_num)
                close_chars.append(crypt_char)
            else:
                close_chars.append(char)
        close_text = "".join(close_chars)
        return close_text

    def encrypt(self, open_text: str, key: int):
        return self._crypt(open_text, key)

    def decrypt(self, close_text: str, key: int):
        return self._crypt(close_text, key, decrypt=True)

    def bruteforce(self, close_text):
        attempts = {}
        for key in range(32):
            attempts[key] = self.decrypt(close_text, key)
        return attempts
