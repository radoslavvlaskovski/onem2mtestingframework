welcome_message = "Welcome to the OneM2M Testing Framework\n" \
                  + "The currently Pre-Build Tests: " + " \n" \
                  + "functional tests, " + " \n" \
                  + "behaviour tests " + " \n" \
                  + "syntax tests\n" \
                  + "For a list of commands either type help or refer to the User Documentation\n" \
                  + "To leave type quit or q\n\n"

help_message = " These are the console commands for the different test types: " + " \n" \
               + "Functional tests: " + " \n" \
               + "CREATE: create <url> <expected status code> <json> " + " \n\n" \
               + "RETRIEVE: retrieve <url> <expected status code>" + " \n" \
               + "UPDATE: update <url> <expected status code> <json>" + " \n" \
               + "DELETE: delete <url> <expected status code> <json>" + " \n\n" \
               + "Behaviour tests: " + " \n\n" \
               + "Custom: behaviour custom <test file>" + " \n" \
               + "Create Create: behaviour cc <url> <json>" + " \n" \
               + "Create Delete: behaviour cd <url> <json>" + " \n" \
               + "Create Retrieve Delete: behaviour crd <url_create> <json> <url retrieve | delete>" + " \n" \
               + "Create Update Retrieve Delete: behaviour curd <url_create> <json create> <url update | retrieve |" \
                 " delete> <json update>" + " \n" \
               + "Create Retrieve Update Retrieve Delete: behaviour crurd <url_create> <json create> <url update |" \
                 " retrieve | delete> <json update>" + " \n" \
               + "Create Delete Delete: behaviour cdd <url_create> <json> <url delete>" + " \n" \
               + "Create Delete Retrieve: behaviour cdr <url_create> <json> <url retrieve | delete>" + " \n" \
               + "Create Delete Update: behaviour cdu <url_create> <json create> <url update | delete> <json update>" + " \n\n" \
               + "Syntax tests: " + " \n\n" \
               + "Test syntax of response: syntax response <method><url> [json]" + " \n" \
               + "Test pure OneM2M from JSON: syntax json <method> <json>" + " \n\n" \
               + "For more information on what each test does read the User Documentation " + " \n"

wrong_command_message = "\n Test type is not recognised \n To see a list of all implemented test types and how to" \
                        " execute them type: help\n\n"
