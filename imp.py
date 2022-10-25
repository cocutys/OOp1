import os
import colorama
import tcolors
from envparse import env
env.read_envfile('options.env')
tcolors.cprint(tcolors.Color.BRIGHT_BLUE + colorama.Back.BLACK + os.environ.get('USER_NAME'))
print(os.environ.get('PASSWORD'))
