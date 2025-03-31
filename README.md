# Network
Network Automation tasks based on different use-cases

Create a Command  dictionary that has three configuration items - Key Value Pairs
 * description
 * speed
 * duplex

 Each item's Key has is a network feature to configure, and each item's value is the start of a command string that will configure that respective feature.

The features are:
 * description
 * speed
 * duplex

 Ensuring to set the values of the Dictionary have {} braces to ensure we use format() method of strings to insert variables

 see the method support from strings

 >>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


COMMANDS = {
    'description': 'description {}',
    'speed': 'speed {}',
    'duplex': 'duplex {}'
}

print(COMMANDS)
type(COMMANDS)

Create a new CONFIG_PARAMS dictionary that is used to dictate which command follows after the key words

CONFIG_PARAMS = {
    'description': 'auto description by Python',
    'speed': '1000',
    'duplex': 'auto'
}

Loop using a for loop to iterate through the **CONFIG_PARAMS** dictionary using the items() built in function for dictionaries. 

As the iteration happens, use the key from **CONFIG_PARAMS** dictionary and use that to match the right value to form a complete commmand string from the **COMMANDS** dictionary

Use the same Key structure to make this possible. **COMMANDS** dictionary stores the command template while the **CONFIG_PARAMS** has the specific command values 


The result is as show below 

![Screenshot 2025-03-31 at 21 33 55](https://github.com/user-attachments/assets/a2b53e81-7857-4193-81d9-6910109d4b41)
