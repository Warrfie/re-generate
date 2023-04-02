import re
from re_generate import re_generate, re_generator

def test_strip_regular_and_singleton(): #must be run after test_complex_regular()
    reg_exr = r'[ M]{2} [ M]{6}[ M]'
    generated_str = re_generate(reg_exr)
    print(generated_str)
    assert generated_str[0] != " " and generated_str[-1] != " "
    assert re.match(reg_exr, generated_str)

def test_bracers_syntax():
    reg_exr = r"Hi, my name is (david|oxana)"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)

def test_bracers_whith_syntax():
    reg_exr = r"(Hi, my name is (david|oxana)){1,7}"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)

def test_1():
    reg_exr = r"([УКЕНХВАРОСМТYKEHXBAPOCMT][0-9]{3}[УКЕНХВАРОСМТYKEHXBAPOCMT]{2}[0-9]{2,3}|[УКЕНХВАРОСМТYKEHXBAPOCMT]{2}[0-9]{3}[УКЕНХВАРОСМТYKEHXBAPOCMT][0-9]{2}|[0-9]{4}[УКЕНХВАРОСМТYKEHXBAPOCMT]{2}[0-9]{2}|[УКЕНХВАРОСМТYKEHXBAPOCMT]{2}[0-9]{6})"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)

def test_2():
    reg_exr = r"\([0-9()]{1,30}.\)[^0-9)]{2}"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)

def test_3():
    reg_exr = r"[А-Яа-яёЁIVXLC.()\- '`]{100}gfg(fhf[А-Яа-яёЁIVXLC.()\- '`]{100}|gfhf)gh"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)

def test_4():
    reg_exr = r"69[^0-9]abc[a-zA-Z]22[ 8]"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)