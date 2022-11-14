from re_generate.classes import ReLetter, ReMultiplier


def brackets_divider(in_str, container, left_br, right_br):
    temp = ""
    export_li = []
    for i, val in enumerate(in_str):
        if (val == left_br and i == 0) or (val == left_br and temp == "" and in_str[i - 1] != "\\"):
            temp += val
        elif temp != "" and val == right_br and in_str[i - 1] != "\\":
            temp += val
            export_li.append(container(temp))
            temp = ""
        elif temp != "":
            temp += val
        else:
            if len(export_li) == 0 or not isinstance(export_li[-1], str):
                export_li.append(val)
            else:
                export_li[-1] += val
    return export_li


def re_letters_former(reg_str: str) -> list:
    return brackets_divider(reg_str, ReLetter, "[", "]")


def re_multiplier_former(reg_list: list) -> list:
    temp = []
    for cont in reg_list:
        if isinstance(cont, str):
            for val in brackets_divider(cont, ReMultiplier, "{", "}"):
                temp.append(val)
        else:
            temp.append(cont)
    return temp


def variant_spliter(reg_list: list) -> list:
    for i, container in enumerate(reg_list):
        if isinstance(container, str):
            for j, value in enumerate(container):
                if (value == "|" and j == 0) or (value == "|" and container[j - 1] != "\\"):
                    left = (reg_list[:i] + [container[:j]]) if container[:j] != "" else reg_list[:i]
                    right = ([container[j + 1:]] + reg_list[i + 1:]) if container[j + 1:] != "" else reg_list[i + 1:]
                    return [left, *variant_spliter(right)]
    return [reg_list]


def string_divider(reg_list: list) -> list:
    temp = []
    for container in reg_list:
        if isinstance(container, str):
            for i, value in enumerate(container):
                if value == "\\" and container[i + 1] == "\\":
                    temp.append(value)
                elif value != "\\":
                    temp.append(value)
        else:
            temp.append(container)
    return temp


def re_letters_multiplier(reg_list: list) -> list:
    temp = []
    for i, container in enumerate(reg_list):
        if isinstance(container, ReMultiplier):
            for _ in range(container.regul):
                temp.append(reg_list[i - 1])
        elif i + 1 == len(reg_list) or not isinstance(reg_list[i + 1], ReMultiplier):
            temp.append(container)
    return temp


def re_letters_activator(reg_list: list, char_lib: str, will_be_stripped: bool) -> list:
    temp = []
    if will_be_stripped:
        for i, container in enumerate(reg_list):
            if isinstance(container, ReLetter):
                if i == 0 or i + 1 == len(reg_list):
                    temp.append(container.reg_string_generator(char_lib, True))
                else:
                    temp.append(container.reg_string_generator(char_lib))
            else:
                assert i != 0 or container != " ", "Can't form string witch will be splitted"
                temp.append(container)
    else:
        for container in reg_list:
            if isinstance(container, ReLetter):
                temp.append(container.reg_string_generator(char_lib))
            else:
                temp.append(container)
    return temp
