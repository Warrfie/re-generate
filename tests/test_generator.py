import re
import re_generate


def test_letter():
    reg_exr = r"abcd"
    assert re.match(reg_exr, re_generate.get_str(reg_exr))


def test_square_brackets():
    reg_exr = r"[abcd]e"
    assert re.match(reg_exr, re_generate.get_str(reg_exr))


def test_not_in_square_brackets():
    reg_exr = r"[^abcd]e"
    assert re.match(reg_exr, re_generate.get_str(reg_exr))


def test_braces_quantifiers():
    reg_exr = r"abcde{1}"
    assert re.match(reg_exr, re_generate.get_str(reg_exr))


def test_range_braces_quantifiers():
    reg_exr = r"abcde{1,3}"
    assert re.match(reg_exr, re_generate.get_str(reg_exr))


def test_or_syntax():
    reg_exr = r"a|b"
    assert re.match(reg_exr, re_generate.get_str(reg_exr))

def test_complex_regular():
    re_generate.main_generator.will_be_stripped = True
    reg_exr = r'[^IVXLCDM]{1,7}[-][А-ЯЁ]{2}[ ][0-9]{6}'
    generated_str = re_generate.get_str(reg_exr)
    assert generated_str[0] != " " and generated_str[-1] != " "
    assert re.match(reg_exr, generated_str)

def test_strip_regular():
    re_generate.main_generator.will_be_stripped = True
    reg_exr = r'[ M][ M]{6}'
    generated_str = re_generate.get_str(reg_exr)
    assert generated_str[0] != " " and generated_str[-1] != " "
    assert re.match(reg_exr, generated_str)