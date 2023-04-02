import re
from re_generate import re_generate, re_generator, ReGenerator


def test_letter():
    reg_exr = r"abcd"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)


def test_square_brackets():
    reg_exr = r"[abcd]e"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)


def test_not_in_square_brackets():
    reg_exr = r"[^abcd]e"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)


def test_braces_quantifiers():
    reg_exr = r"abcde{1}"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)


def test_range_braces_quantifiers():
    reg_exr = r"abcde{1,3}"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)


def test_or_syntax():
    reg_exr = r"a|b"
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert re.match(reg_exr, generated_str)

def test_complex_regular():
    re_generator.will_be_stripped = True
    reg_exr = r'[^IVXLCDM]{1,7}[-][А-ЯЁ]{2}[ ][0-9]{6}'
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert generated_str[0] != " " and generated_str[-1] != " "
    assert re.match(reg_exr, generated_str)

def test_strip_regular_and_singleton(): #must be run after test_complex_regular()
    reg_exr = r'[ M]{2} [ M]{6}[ M]'
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert generated_str[0] != " " and generated_str[-1] != " "
    assert re.match(reg_exr, generated_str)

def test_or_regular():
    re_generator.will_be_stripped = True
    reg_exr = r'[^IVXLCDM]{1,7}[-]|[А-ЯЁ]{2}[ ][0-9]{6}'
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert generated_str[0] != " " and generated_str[-1] != " "
    assert re.match(reg_exr, generated_str)

def test_brackets_regular():
    re_generator.will_be_stripped = True
    reg_exr = r'[^IVXLCDM]{1,7}([-]|[А-ЯЁ]{2})[ ][0-9]{6}'
    generated_str = re_generate(reg_exr)
    print()
    print(generated_str)
    assert generated_str[0] != " " and generated_str[-1] != " "
    assert re.match(reg_exr, generated_str)

