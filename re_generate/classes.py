import random
import re


class ReLetter:
    def __init__(self, regul):
        self.regul = regul
        self.amount = 1

    def __repr__(self):
        return f"ReLetter class({self.regul})"

    def __str__(self):
        return f"ReLetter class({self.regul})"

    def reg_string_generator(self, char_lib: str, not_space=False) -> str:
        chars = ""
        reg = self.regul
        if "[^" in reg:
            chars = re.findall(reg, char_lib)
            if not_space:
                chars = "".join(chars).replace(" ", "")
                assert len(chars) > 0, "Can't form string witch will be splitted"
            return "".join([random.choice(chars) for _ in range(self.amount)])
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
        return "".join([random.choice(chars) for _ in range(self.amount)])


class ReMultiplier:
    def __init__(self, regul):
        if "," in regul:
            mult_range = range(int(regul.split(",")[0][1:]), int(regul.split(",")[1][:-1]))
            regul = random.choice(mult_range)
        else:
            regul = int(regul[1:-1])
        self.regul = regul

    def __repr__(self):
        return f"ReDiv class({self.regul})"

    def __str__(self):
        return f"ReDiv class({self.regul})"
