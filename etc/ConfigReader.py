"""
Class that reads the config file
and sets the options to the Log
"""

class ConfigReader:

    options = {
        "console_print": 0,
        "log_to_file": 0,
        "gui": 0
    }

    def __init__(self,sender):
        self.sender = sender

    def read_config(self):

        config = open("config", "r")

        lines = config.readlines()

        for i in range(0, len(lines)):
            args = lines[i].split(" ")

            for key in self.options.keys():
                if args[0] == key:
                    self.options[key] = args[1]

        config.close()

    def update_logging_options(self):

        if int(self.options["console_print"]) == 1:
            self.sender.Log.printer = True
        elif int(self.options["console_print"]) != 0 and int(self.options["console_print"]) != 1:
            print("Problem with the config\n"
                  + "console_print should be set to 1 or 0\n\n")

    def get_gui_option(self):

        return self.options['gui']
