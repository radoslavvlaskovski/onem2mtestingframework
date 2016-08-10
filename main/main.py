from etc import ConsoleReader
from Sender import SenderHTTP
from etc import ConfigReader, gui_main


def main():

    sender = SenderHTTP.SenderHTTP()

    config = ConfigReader.ConfigReader(sender)
    config.read_config()
    config.update_logging_options()

    if int(config.get_gui_option()) == 1:
        gui_main.launch(sender)

    reader = ConsoleReader.ConsoleReader(sender)
    reader.read()

    return 0


if __name__ == "__main__":
    main()
