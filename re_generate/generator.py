import copy
import random
from re_generate.cfg_constants import *

from re_generate.handlers import *


class ReGenerator:
    will_be_stripped = WILL_BE_STRIPPED
    char_lib = CHAR_LIB
    amount = 1

    def __init__(self, prep=None):
        self.prep = copy.deepcopy(prep)

    def re_generator(self, regular_expression="") -> str:
        if self.prep is None:
            self.prep = re_letters_former(regular_expression)
            self.prep = re_multiplier_former(self.prep)
        self.prep = re_parentheses_content(self.prep)
        self.prep = random.choice(variant_spliter(self.prep))
        self.prep = string_divider(self.prep)
        self.prep = re_letters_multiplier(self.prep)
        self.prep = re_letters_activator(self.prep, self.char_lib, self.will_be_stripped)
        if len(self.prep) == 0:
            self.prep = None
            raise "Wrong ReGex! can't generate anything from it!"
        generated_str = "".join(self.prep)
        self.prep = None
        return generated_str

    def re_generator_list(self, regular_expression: str, amount: int) -> list:
        return [self.re_generator(regular_expression) for _ in range(amount)]
