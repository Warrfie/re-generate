import re
import random
from constants import *

def reg_string_generator(i_reg):  # Получает строку формата [.+]{\d+} или [.+]
    chars = ""
    length = 1
    if i_reg[-1] == "}":
        length_st = re.findall(r"\{[0-9,]+\}", i_reg)[0]
        i_reg = i_reg.replace(length_st, "")
        if "," in length_st:
            length_range = re.findall(r"\d+", length_st)
            length = random.randint(int(length_range[0]), int(length_range[1]))
        else:
            length = int(length_st[1:-1])
    if "[^" in i_reg:
        chars = re.findall(i_reg, all_chars)
        return "".join(random.choice(chars) for _ in range(length))
    i_reg = i_reg[1:-1]
    if "\\" in i_reg:
        spes = re.findall(r"\\.", i_reg)
        for let in spes:
            chars += let[1]
            i_reg = i_reg.replace(let, "")
    if "-" in i_reg:
        spes = re.findall(r".-.", i_reg)
        for let in spes:
            chars += "".join(chr(i + ord(let[0])) for i in range(1 + ord(let[2]) - ord(let[0])))
            i_reg = i_reg.replace(let, "")
    chars += i_reg
    return "".join(random.choice(chars) for _ in range(length))


def reg_spliter(i_reg: str):
    all_regs = re.findall(r'\[.*?[^\\]\]\{?[0-9,]*\}?', i_reg)
    for reg in all_regs:
        i_reg = i_reg.replace(reg, reg_string_generator(reg), 1)
    return i_reg


def re_generate(i_reg):
    while True:
        if "|" in i_reg:
            splited_reg = i_reg.split("|")
            flag = True
            while flag:
                flag = False
                for i in range(len(splited_reg)):
                    open_sym = splited_reg[i].count("[")
                    close_sym = splited_reg[i].count("]")
                    if open_sym != close_sym:
                        splited_reg[i] = splited_reg[i] + "|" + splited_reg[i + 1]
                        del splited_reg[i + 1]
                        flag = True
                        break
            if len(splited_reg) == 1:
                return reg_spliter(i_reg)
            generated_string = random.choice([re_generate(variant) for variant in splited_reg])
        else:
            generated_string = reg_spliter(i_reg)

        assert len(generated_string) > 0, "Неверное регулярное выражение, строка не сгенерирована"
        stripted_string = generated_string.strip()
        if len(generated_string) == len(stripted_string) and len(stripted_string) > 0:
            return stripted_string
