[![PyPi Package Version](https://img.shields.io/pypi/v/re-generate.svg)](https://pypi.python.org/pypi/re-generate)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/re-generate.svg)](https://pypi.python.org/pypi/re-generate)
[![PyPi status](https://img.shields.io/pypi/status/re-generate.svg?style=flat-square)](https://pypi.python.org/pypi/re-generate)

# <p align="center">Re-Generate

<p align="center">A simple and light package for QA development which can generate random strings via RegExr.</p>
<p align="center">Not all RegExr mechanics are available now. But you can use all base methods and generate any string.</p>

# <p align="center">Summary</a>

##What RegExr syntax supported

|                type                | is supported       |
|:----------------------------------:|--------------------|
|         [] square brackets         | :white_check_mark: |
|        [^] square brackets         | :white_check_mark: |
|       {} braces quantifiers        | :white_check_mark: |
|         {i,j} multiplyers          | :white_check_mark: |
|            	&#124;  or             | :white_check_mark: |
|             () groups              | :x:                |
|  \n,\s,\d...etc reserved samples   | :x:                |
|    *?,+?,?? greedy quantifiers     | :x:                |
|       *,+,? lazy quantifiers       | :x:                |

##Main functionality
How generate
```python
import re_generate
print(re_generate.get_str(r"69[0-9]abc[a-zA-Z]228"))
```
    '693abcb228'
How generate several strings ot once
```python
import re_generate
print(re_generate.get_list(r"69[0-9]abc[a-zA-Z]228"), 10)
```
    ['694abcO228', '693abcG228', '692abcV228', '696abcy228', '693abca228', '690abcb228', '694abcD228', '696abck228', '696abcJ228', '692abca228']

##What you can configue
If you want to use your own library
```python
import re_generate
re_generate.main_generator.char_lib = "你f好п我Э的$中(国*朋Ъ友1234+=\/,."
```

Sometimes you need generate string without spaces at begin and end, like after .strip() function.
```python
import re_generate
re_generate.main_generator.will_be_splitted = True
```
#Tips and tricks
In large project you can link that lib throw cfg py file like that
```
cfg.py
```

```python
import re_generate
re_generate.main_generator.char_lib = "你f好п我Э的$中(国*朋Ъ友1234+=\/,."
re_generate.main_generator.will_be_splitted = True
your_func = re_generate
```
and use it in your project
```
your_code.py
```

```python
from cfg import your_func
print(your_func.get_str(r"69[^0-9]abc[a-zA-Z]22[ 8]"))
```
    '69我abcb228'



