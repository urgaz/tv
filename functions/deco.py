from functions.main import *


def print_ip(func):
    def func_arguments(*args, **kwargs):
        request = args[0]
        user = get_ip(request)
        print(user)
        if user == '192.168.8.8':
            print('||||||||||\n|        |\n|        |\n||||||||||')
#         else:
#             print("""

# |               |
#  |             |
#   |           |
#    |         |
#     |       |
#      |     |
#       |   |
#        | |
#         | 
#             """)
        return func(*args, **kwargs)
    return func_arguments