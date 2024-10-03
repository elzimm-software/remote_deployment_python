from menu import Menu
from run_bash_cmd_function import run_bash_cmd

m = Menu()
m.add_option("Check available memory")
m.add_option("View network connections")
m.add_option("Display free ram and swap")
option = m.get_input()
run_bash_cmd(option)