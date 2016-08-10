"""

File created to manage how tests are  read from the console

"""

from Mappings import BasicPrimitives as bp, PrimitiveHTTP
from Test import FunctionalTests as ft, SyntaxTestsHTTP, BehaviourTests as bt, SyntaxTests as st, ResponseParameterTests as rpt
from etc import TestLineReader as reader, TestFileReader, messages


class ConsoleReader:
    def __init__(self, sender):
        self.sender = sender
        self.print_instructions()

    def print_instructions(self):

        print(messages.welcome_message)

    def read(self):

        p = bp.response_primitive
        phttp = PrimitiveHTTP.PrimitiveHTTP(p)

        syntax_tester = SyntaxTestsHTTP.SyntaxTests(self.sender, phttp)
        om2m_syntax_tester = st.SyntaxTests(self.sender.Log)

        functional_tests = ft.FunctionalTests(self.sender)
        behaviour_t = bt.BehaviorTests(self.sender)
        parameter_functional_tests = rpt.ResponseParameterTests(self.sender)

        console_reader = reader.TestLineReader(functional_tests, syntax_tester, behaviour_t, om2m_syntax_tester, parameter_functional_tests)

        while (1):
            cmd = raw_input("")
            args = cmd.split(" ")

            if cmd.lower() == "quit" or cmd.lower() == "q":
                break

            elif cmd.lower() == "print":
                self.sender.Log.printer = not self.sender.Log.printer
	    elif cmd.lower() == "help":
		print(messages.help_message)

            elif len(args) == 2:
                if args[0] == "testfile":
                    TestFileReader.read_test_file(args[1], console_reader)

            else:
                console_reader.args_read(args)
