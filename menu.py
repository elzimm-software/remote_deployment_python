
class Menu:
    """
    Menu for a CLI.
    """
    def __init__(self):
        """
        Constructs a menu with quit option.
        """
        # Since quiting is handled by this class, Quit should always be an option.
        self._options = ["Quit"]

    def add_option(self, option: str):
        """
        Adds an option to the menu.

        :param option: the option to add
        """
        self._options.insert(self._options.__len__() - 1, option)

    def get_input(self):
        """
        Displays the menu with corresponding numbers
        and receives and validates the user's selection.

        :return: the user's selected option
        """
        option = 0
        while True:
            for (i, op) in enumerate(self._options):
                print(i + 1, op)
            option_str = input()
            if option_str == "Q":
                quit(0)
            else:
                option = int(option_str)
            if option > self._options.__len__() or option < 1:
                print("Invalid input.\nPlease enter a number from 1 to", self._options.__len__(), ".")
            else:
                return option
