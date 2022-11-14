import random
from re_generate.cfg_constants import *

from re_generate.handlers import re_letters_former, re_multiplier_former, variant_spliter, string_divider, \
    re_letters_multiplier, re_letters_activator


class ReGenerator:

    def __init__(self):
        self.will_be_stripped = WILL_BE_STRIPPED
        self.char_lib = CHAR_LIB

    def re_generator(self, regular_expression: str) -> str:
        temp = re_letters_former(regular_expression)
        temp = re_multiplier_former(temp)
        temp = random.choice(variant_spliter(temp))
        temp = string_divider(temp)
        temp = re_letters_multiplier(temp)
        temp = re_letters_activator(temp, self.char_lib, self.will_be_stripped)
        assert len(temp) > 0, "Wrong ReGex! can't generate anything from it!"
        return "".join(temp)

    def re_generator_list(self, regular_expression: str, amount: int) -> list:
        return [self.re_generator(regular_expression) for _ in range(amount)]
