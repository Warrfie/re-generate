import random
import re


class ReLetter:
    def __init__(self, regul):
        self.regul = regul

    def __repr__(self):
        return f"ReLetter class({self.regul})"

    def __str__(self):
        return f"ReLetter class({self.regul})"

    def reg_string_generator(self, char_lib, not_space=False):  # Получает строку формата [.+]{\d+} или [.+]
        chars = ""
        reg = self.regul
        if "[^" in reg:
            chars = re.findall(reg, char_lib)
            if not_space:
                chars = "".join(chars).replace(" ", "")
                assert len(chars) > 0, "Can't form string witch will be splitted"
            return random.choice(chars)
        reg = reg[1:-1]
        if "\\" in reg:
            spes = re.findall(r"\\.", reg)
            for let in spes:
                chars += let[1]
                reg = reg.replace(let, "")
        if "-" in reg:
            spes = re.findall(r".-.", reg)
            for let in spes:
                chars += "".join(chr(i + ord(let[0])) for i in range(1 + ord(let[2]) - ord(let[0])))
                reg = reg.replace(let, "")
        chars += reg
        if not_space:
            chars = "".join(chars).replace(" ", "")
            assert len(chars) > 0, "Can't form string witch will be splitted"
        return random.choice(chars)


class ReMultiplier:
    def __init__(self, regul):
        if len(regul) == 3:
            regul = int(regul[1])
        else:
            mult_range = range(int(regul.split(",")[0][1:]), int(regul.split(",")[1][:-1]))
            regul = random.choice(mult_range)
        self.regul = regul

    def __repr__(self):
        return f"ReDiv class({self.regul})"

    def __str__(self):
        return f"ReDiv class({self.regul})"
