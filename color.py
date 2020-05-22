from os import system, name
class Color:
   if name == 'nt':
      PURPLE = '\x1b[35m'
      CYAN = '\x1b[36m'
      DARKCYAN = '\x1b[96m'
      BLUE = '\x1b[34m'
      GREEN = '\x1b[32m'
      BOLD = '\x1b[1m'
      YELLOW = '\x1b[33m'
      RED = '\x1b[31m'
      END = '\x1b[0m'
   else:
      PURPLE = '\033[95m'
      CYAN = '\033[96m'
      DARKCYAN = '\033[36m'
      BLUE = '\033[94m'
      GREEN = '\033[92m'
      BOLD = '\033[1m'
      YELLOW = '\033[93m'
      RED = '\033[91m'
      END = '\033[0m'
if __name__ == "__main__":
    print(name)
    print(Color.RED + 'Hello World !' + Color.END)