# from module_1 import funcs
from module_1.funcs import my_func
# from module_2.submodule_1.tools import reverse_string
# from module_2 import *
# from module_1.funcs import *

import module_2

# my_func()

# result = reverse_string("Hello")

result = module_2.reverse_string("Hello!")
print(result)