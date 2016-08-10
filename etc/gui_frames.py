"""

The creation of the different frames 
is implemented here
For every frame there is a separate function

 """

try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from Test import FunctionalTests as ft, BehaviourTests as bt, SyntaxTestsHTTP as st, ResponseParameterTests as rpt
from Mappings import BasicPrimitives as bp, PrimitiveHTTP as phttp
import json
from etc import gui_helper, ParameterChecking as checker
import tkMessageBox


def create_functional_frame(subframe, sender):
    functional_tests = ft.FunctionalTests(sender)

    result_var = StringVar()
    create_var = BooleanVar()
    retrieve_var = BooleanVar()
    update_var = BooleanVar()
    delete_var = BooleanVar()

    url_label = Label(subframe, text="URL")
    url_entry = Entry(subframe, width=60)

    expected_entry = Entry(subframe)
    expected_label = Label(subframe, text="Expected Response Status")

    json_text = Text(subframe, width=60, height=12)
    json_label = Label(subframe, text="JSON (if needed)")

    json_scrollb = Scrollbar(subframe, command=json_text.yview)
    json_text['yscrollcommand'] = json_scrollb.set

    checkbox_create = Checkbutton(subframe, text="CREATE", variable=create_var)
    checkbox_retrieve = Checkbutton(subframe, text="RETRIEVE", variable=retrieve_var)
    checkbox_update = Checkbutton(subframe, text="UPDATE", variable=update_var)
    checkbox_delete = Checkbutton(subframe, text="DELETE", variable=delete_var)

    result_message = Message(subframe, textvariable=result_var)

    def callback():
        if create_var.get():
            check = checker.check_parameters_simple(url_entry.get(), expected_entry.get())

            if isinstance(check, str):
                tkMessageBox.showinfo("ERROR", check)
            else:
                result_var.set(
                    functional_tests.test_create_request_from_json(url_entry.get(), _retrieve_input(json_text),
                                                                   expected_entry.get()))
        if retrieve_var.get():
            check = checker.check_parameters_simple(url_entry.get(), expected_entry.get())

            if isinstance(check, str):
                tkMessageBox.showinfo("ERROR", check)
            else:
                result_var.set(
                    functional_tests.test_retrieve_request(url_entry.get(), expected_entry.get()))

        if update_var.get():
            check = checker.check_parameters_simple(url_entry.get(), expected_entry.get())

            if isinstance(check, str):
                tkMessageBox.showinfo("ERROR", check)
            else:
                result_var.set(
                    functional_tests.test_update_request_from_json(url_entry.get(), _retrieve_input(json_text),
                                                                   expected_entry.get()))
        if delete_var.get():
            check = checker.check_parameters_simple(url_entry.get(), expected_entry.get())

            if isinstance(check, str):
                tkMessageBox.showinfo("ERROR", check)
            else:
                result_var.set(
                    functional_tests.test_delete_request(url_entry.get(), expected_entry.get()))

    button_send = Button(subframe, text="Test", command=callback)

    result_message.grid(row=6)
    button_send.grid(row=5, column=1)

    json_label.grid(row=2, column=0)
    json_text.grid(row=2, column=1)
    json_scrollb.grid(row=2, column=2, sticky='nsew')

    expected_entry.grid(row=1, column=1)
    expected_label.grid(row=1, column=0)

    url_entry.grid(row=0, column=1)
    url_label.grid(row=0, column=0)

    checkbox_create.grid(row=3, column=0)
    checkbox_retrieve.grid(row=3, column=1)
    checkbox_update.grid(row=3, column=2)
    checkbox_delete.grid(row=3, column=3)


def create_behaviour_frame(subframe, sender):
    behaviour_tests = bt.BehaviorTests(sender)

    cc_result_var = StringVar()

    cc_label = Label(subframe, text="Test Creating the same resource twice - Response should be CONFLICT",
                     font=("Helvetica", 14))

    cc_url_label = Label(subframe, text="URL: ")
    cc_url_entry = Entry(subframe, width=60)

    cc_json_text = Text(subframe, width=60, height=12)
    cc_json_label = Label(subframe, text="JSON")
    cc_json_scrollb = Scrollbar(subframe, command=cc_json_text.yview)
    cc_json_text['yscrollcommand'] = cc_json_scrollb.set

    cc_result_message = Message(subframe, textvariable=cc_result_var)

    def cc_callback():
        check = checker.check_url(cc_url_entry.get())

        if check == False:
            tkMessageBox.showinfo("ERROR", "Wrong URL")
        else:
            cc_result_var.set(
                behaviour_tests.test_create_create(cc_url_entry.get(), _retrieve_input(cc_json_text)))

    cc_button = Button(subframe, text="Test", command=cc_callback)

    cc_label.grid(row=0)

    cc_url_label.grid(row=2, column=0)
    cc_url_entry.grid(row=2, column=1)
    cc_json_label.grid(row=4, column=0)
    cc_json_text.grid(row=4, column=1)
    cc_json_scrollb.grid(row=4, column=2, sticky='nsew')
    cc_button.grid(row=5, column=0)
    cc_result_message.grid(row=6)

    cgd_result_var = StringVar()

    cgd_label = Label(subframe, text="Test Creating Retrieving and Deleting a resource",
                      font=("Helvetica", 14))

    cgd_url_label1 = Label(subframe, text="URL Create: ")
    cgd_url_entry1 = Entry(subframe, width=60)
    cgd_url_label2 = Label(subframe, text="URL Retrieve and Delete: ")
    cgd_url_entry2 = Entry(subframe, width=60)

    cgd_json_text = Text(subframe, width=60, height=12)
    cgd_json_label = Label(subframe, text="JSON")
    cgd_json_scrollb = Scrollbar(subframe, command=cgd_json_text.yview)
    cgd_json_text['yscrollcommand'] = cgd_json_scrollb.set

    cgd_result_message = Message(subframe, textvariable=cgd_result_var)

    def cgd_callback():
        urls = list()
        urls.append(cgd_url_entry1.get())
        urls.append(cgd_url_entry2.get())

        check1 = checker.check_url(cgd_url_entry1.get())
        check2 = checker.check_url(cgd_url_entry2.get())

        if check1 == False or check2 == False:
            tkMessageBox.showinfo("ERROR", "Wrong URL")
        else:
            cgd_result_var.set(
                behaviour_tests.test_create_retrieve_delete(urls, _retrieve_input(cgd_json_text)))

    cgd_button = Button(subframe, text="Test", command=cgd_callback)

    cgd_label.grid(row=8)

    cgd_url_label1.grid(row=10, column=0)
    cgd_url_entry1.grid(row=10, column=1)
    cgd_url_label2.grid(row=11, column=0)
    cgd_url_entry2.grid(row=11, column=1)
    cgd_json_label.grid(row=13, column=0)
    cgd_json_text.grid(row=13, column=1)
    cgd_json_scrollb.grid(row=13, column=2, sticky='nsew')
    cgd_button.grid(row=14, column=0)
    cgd_result_message.grid(row=15)

    cd_result_var = StringVar()

    cd_label = Label(subframe, text="Test Creating and Deleting a resource",
                     font=("Helvetica", 14))

    cd_url_label1 = Label(subframe, text="URL Create: ")
    cd_url_entry1 = Entry(subframe, width=60)
    cd_url_label2 = Label(subframe, text="URL Delete: ")
    cd_url_entry2 = Entry(subframe, width=60)

    cd_json_text = Text(subframe, width=60, height=12)
    cd_json_label = Label(subframe, text="JSON")
    cd_json_scrollb = Scrollbar(subframe, command=cd_json_text.yview)
    cd_json_text['yscrollcommand'] = cd_json_scrollb.set

    cd_result_message = Message(subframe, textvariable=cd_result_var)

    def cd_callback():
        urls = list()
        urls.append(cd_url_entry1.get())
        urls.append(cd_url_entry2.get())

        check1 = checker.check_url(cd_url_entry1.get())
        check2 = checker.check_url(cd_url_entry2.get())

        if check1 == False or check2 == False:
            tkMessageBox.showinfo("ERROR", "Wrong URL")
        else:
            cd_result_var.set(
                behaviour_tests.test_create_delete(urls, _retrieve_input(cd_json_text)))

    cd_button = Button(subframe, text="Test", command=cd_callback)

    cd_label.grid(row=17)

    cd_url_label1.grid(row=19, column=0)
    cd_url_entry1.grid(row=19, column=1)
    cd_url_label2.grid(row=20, column=0)
    cd_url_entry2.grid(row=20, column=1)
    cd_json_label.grid(row=22, column=0)
    cd_json_text.grid(row=22, column=1)
    cd_json_scrollb.grid(row=22, column=2, sticky='nsew')
    cd_button.grid(row=23, column=0)
    cd_result_message.grid(row=24)

    cdd_result_var = StringVar()

    cdd_label = Label(subframe, text="Test Creating Deleting and Deleting a resource",
                      font=("Helvetica", 14))

    cdd_url_label1 = Label(subframe, text="URL Create: ")
    cdd_url_entry1 = Entry(subframe, width=60)
    cdd_url_label2 = Label(subframe, text="URL Delete: ")
    cdd_url_entry2 = Entry(subframe, width=60)

    cdd_json_text = Text(subframe, width=60, height=12)
    cdd_json_label = Label(subframe, text="JSON")
    cdd_json_scrollb = Scrollbar(subframe, command=cdd_json_text.yview)
    cdd_json_text['yscrollcommand'] = cdd_json_scrollb.set

    cdd_result_message = Message(subframe, textvariable=cdd_result_var)

    def cdd_callback():
        urls = list()
        urls.append(cdd_url_entry1.get())
        urls.append(cdd_url_entry2.get())

        check1 = checker.check_url(cdd_url_entry1.get())
        check2 = checker.check_url(cdd_url_entry2.get())

        if check1 == False or check2 == False:
            tkMessageBox.showinfo("ERROR", "Wrong URL")
        else:
            cdd_result_var.set(
                behaviour_tests.test_create_delete_delete(urls, _retrieve_input(cdd_json_text)))

    cdd_button = Button(subframe, text="Test", command=cdd_callback)

    cdd_label.grid(row=25)

    cdd_url_label1.grid(row=26, column=0)
    cdd_url_entry1.grid(row=26, column=1)
    cdd_url_label2.grid(row=27, column=0)
    cdd_url_entry2.grid(row=27, column=1)
    cdd_json_label.grid(row=29, column=0)
    cdd_json_text.grid(row=29, column=1)
    cdd_json_scrollb.grid(row=29, column=2, sticky='nsew')
    cdd_button.grid(row=30, column=0)
    cdd_result_message.grid(row=31)

    cdr_result_var = StringVar()

    cdr_label = Label(subframe, text="Test Creating Deleting and Retrieving a resource",
                      font=("Helvetica", 14))

    cdr_url_label1 = Label(subframe, text="URL Create: ")
    cdr_url_entry1 = Entry(subframe, width=60)
    cdr_url_label2 = Label(subframe, text="URL Delete and Retrieve: ")
    cdr_url_entry2 = Entry(subframe, width=60)

    cdr_json_text = Text(subframe, width=60, height=12)
    cdr_json_label = Label(subframe, text="JSON")
    cdr_json_scrollb = Scrollbar(subframe, command=cdr_json_text.yview)
    cdr_json_text['yscrollcommand'] = cdr_json_scrollb.set

    cdr_result_message = Message(subframe, textvariable=cdr_result_var)

    def cdr_callback():
        urls = list()
        urls.append(cdr_url_entry1.get())
        urls.append(cdr_url_entry2.get())

        check1 = checker.check_url(cdr_url_entry1.get())
        check2 = checker.check_url(cdr_url_entry2.get())

        if check1 == False or check2 == False:
            tkMessageBox.showinfo("ERROR", "Wrong URL")
        else:
            cdr_result_var.set(
                behaviour_tests.test_create_delete_get(urls, _retrieve_input(cdr_json_text)))

    cdr_button = Button(subframe, text="Test", command=cdr_callback)

    cdr_label.grid(row=32)

    cdr_url_label1.grid(row=33, column=0)
    cdr_url_entry1.grid(row=33, column=1)
    cdr_url_label2.grid(row=34, column=0)
    cdr_url_entry2.grid(row=34, column=1)
    cdr_json_label.grid(row=36, column=0)
    cdr_json_text.grid(row=36, column=1)
    cdr_json_scrollb.grid(row=36, column=2, sticky='nsew')
    cdr_button.grid(row=38, column=0)
    cdr_result_message.grid(row=39)

    cdu_result_var = StringVar()

    cdu_label = Label(subframe, text="Test Creating Deleting and Update a resource",
                      font=("Helvetica", 14))

    cdu_url_label1 = Label(subframe, text="URL Create: ")
    cdu_url_entry1 = Entry(subframe, width=60)
    cdu_url_label2 = Label(subframe, text="URL Delete and Update: ")
    cdu_url_entry2 = Entry(subframe, width=60)

    cdu_json_create_text = Text(subframe, width=60, height=12)
    cdu_json_create_label = Label(subframe, text="JSON CREATE")
    cdu_json_create_scrollb = Scrollbar(subframe, command=cdu_json_create_text.yview)
    cdu_json_create_text['yscrollcommand'] = cdu_json_create_scrollb.set

    cdu_json_update_text = Text(subframe, width=60, height=12)
    cdu_json_update_label = Label(subframe, text="JSON UPDATE")
    cdu_json_update_scrollb = Scrollbar(subframe, command=cdu_json_update_text.yview)
    cdu_json_update_text['yscrollcommand'] = cdu_json_update_scrollb.set

    cdu_result_message = Message(subframe, textvariable=cdu_result_var)

    def cdu_callback():
        urls = list()
        urls.append(cdu_url_entry1.get())
        urls.append(cdu_url_entry2.get())

        check1 = checker.check_url(cdu_url_entry1.get())
        check2 = checker.check_url(cdu_url_entry2.get())

        if check1 == False or check2 == False:
            tkMessageBox.showinfo("ERROR", "Wrong URL")
        else:

            json_c = _retrieve_input(cdu_json_create_text)
            json_u = _retrieve_input(cdu_json_update_text)
            reqs = list()
            reqs.append(json_c)
            reqs.append(json_u)

            cdu_result_var.set(
                behaviour_tests.test_create_delete_update(urls, reqs))

    cdu_button = Button(subframe, text="Test", command=cdu_callback)

    cdu_label.grid(row=40)

    cdu_url_label1.grid(row=41, column=0)
    cdu_url_entry1.grid(row=41, column=1)
    cdu_url_label2.grid(row=42, column=0)
    cdu_url_entry2.grid(row=42, column=1)
    cdu_json_create_label.grid(row=44, column=0)
    cdu_json_create_text.grid(row=44, column=1)
    cdu_json_create_scrollb.grid(row=44, column=2, sticky='nsew')
    cdu_json_update_label.grid(row=46, column=0)
    cdu_json_update_text.grid(row=46, column=1)
    cdu_json_update_scrollb.grid(row=46, column=2, sticky='nsew')
    cdu_button.grid(row=48, column=0)
    cdu_result_message.grid(row=49)

    curd_result_var = StringVar()

    curd_label = Label(subframe, text="Test Create Update Retrieve Delete a resource",
                       font=("Helvetica", 14))

    curd_url_label1 = Label(subframe, text="URL Create: ")
    curd_url_entry1 = Entry(subframe, width=60)
    curd_url_label2 = Label(subframe, text="URL Delete and Update: ")
    curd_url_entry2 = Entry(subframe, width=60)

    curd_json_create_text = Text(subframe, width=60, height=12)
    curd_json_create_label = Label(subframe, text="JSON CREATE")
    curd_json_create_scrollb = Scrollbar(subframe, command=curd_json_create_text.yview)
    curd_json_create_text['yscrollcommand'] = curd_json_create_scrollb.set

    curd_json_update_text = Text(subframe, width=60, height=12)
    curd_json_update_label = Label(subframe, text="JSON UPDATE")
    curd_json_update_scrollb = Scrollbar(subframe, command=curd_json_update_text.yview)
    curd_json_update_text['yscrollcommand'] = curd_json_update_scrollb.set

    curd_result_message = Message(subframe, textvariable=curd_result_var)

    def curd_callback():
        urls = list()
        urls.append(curd_url_entry1.get())
        urls.append(curd_url_entry2.get())

        check1 = checker.check_url(curd_url_entry1.get())
        check2 = checker.check_url(curd_url_entry2.get())

        if check1 == False or check2 == False:
            tkMessageBox.showinfo("ERROR", "Wrong URL")
        else:

            json_c = _retrieve_input(curd_json_create_text)
            json_u = _retrieve_input(curd_json_update_text)
            reqs = list()
            reqs.append(json_c)
            reqs.append(json_u)

            curd_result_var.set(
                behaviour_tests.test_create_update_retrieve_delete(urls, reqs))

    curd_button = Button(subframe, text="Test", command=curd_callback)

    curd_label.grid(row=50)

    curd_url_label1.grid(row=51, column=0)
    curd_url_entry1.grid(row=51, column=1)
    curd_url_label2.grid(row=52, column=0)
    curd_url_entry2.grid(row=52, column=1)
    curd_json_create_label.grid(row=54, column=0)
    curd_json_create_text.grid(row=54, column=1)
    curd_json_create_scrollb.grid(row=54, column=2, sticky='nsew')
    curd_json_update_label.grid(row=56, column=0)
    curd_json_update_text.grid(row=56, column=1)
    curd_json_update_scrollb.grid(row=56, column=2, sticky='nsew')
    curd_button.grid(row=58, column=0)
    curd_result_message.grid(row=59)

    crurd_result_var = StringVar()

    crurd_label = Label(subframe, text="Test Create Retrieve Update Retrieve Delete a resource",
                        font=("Helvetica", 14))

    crurd_url_label1 = Label(subframe, text="URL Create: ")
    crurd_url_entry1 = Entry(subframe, width=60)
    crurd_url_label2 = Label(subframe, text="URL Delete and Update: ")
    crurd_url_entry2 = Entry(subframe, width=60)

    crurd_json_create_text = Text(subframe, width=60, height=12)
    crurd_json_create_label = Label(subframe, text="JSON CREATE")
    crurd_json_create_scrollb = Scrollbar(subframe, command=crurd_json_create_text.yview)
    crurd_json_create_text['yscrollcommand'] = crurd_json_create_scrollb.set

    crurd_json_update_text = Text(subframe, width=60, height=12)
    crurd_json_update_label = Label(subframe, text="JSON UPDATE")
    crurd_json_update_scrollb = Scrollbar(subframe, command=crurd_json_update_text.yview)
    crurd_json_update_text['yscrollcommand'] = crurd_json_update_scrollb.set

    crurd_result_message = Message(subframe, textvariable=crurd_result_var)

    def crurd_callback():
        urls = list()
        urls.append(crurd_url_entry1.get())
        urls.append(crurd_url_entry2.get())

        check1 = checker.check_url(crurd_url_entry1.get())
        check2 = checker.check_url(crurd_url_entry2.get())

        if check1 == False or check2 == False:
            tkMessageBox.showinfo("ERROR", "Wrong URL")
        else:

            json_c = _retrieve_input(crurd_json_create_text)
            json_u = _retrieve_input(crurd_json_update_text)
            reqs = list()
            reqs.append(json_c)
            reqs.append(json_u)

            crurd_result_var.set(
                behaviour_tests.test_create_retrieve_update_retrieve_delete(urls, reqs))

    crurd_button = Button(subframe, text="Test", command=crurd_callback)

    crurd_label.grid(row=60)

    crurd_url_label1.grid(row=61, column=0)
    crurd_url_entry1.grid(row=61, column=1)
    crurd_url_label2.grid(row=62, column=0)
    crurd_url_entry2.grid(row=62, column=1)
    crurd_json_create_label.grid(row=64, column=0)
    crurd_json_create_text.grid(row=64, column=1)
    crurd_json_create_scrollb.grid(row=64, column=2, sticky='nsew')
    crurd_json_update_label.grid(row=66, column=0)
    crurd_json_update_text.grid(row=66, column=1)
    crurd_json_update_scrollb.grid(row=66, column=2, sticky='nsew')
    crurd_button.grid(row=68, column=0)
    crurd_result_message.grid(row=69)


def create_syntax_frame(subframe, sender):
    p = bp.response_primitive
    syntax_tester = st.SyntaxTests(sender, phttp.PrimitiveHTTP(p))

    result_var = StringVar()
    create_var = BooleanVar()
    retrieve_var = BooleanVar()
    update_var = BooleanVar()
    delete_var = BooleanVar()

    url_label = Label(subframe, text="URL")
    url_entry = Entry(subframe, width=60)

    json_text = Text(subframe, width=60, height=12)
    json_label = Label(subframe, text="JSON (if needed)")

    json_scrollb = Scrollbar(subframe, command=json_text.yview)
    json_text['yscrollcommand'] = json_scrollb.set

    checkbox_create = Checkbutton(subframe, text="CREATE", variable=create_var)
    checkbox_retrieve = Checkbutton(subframe, text="RETRIEVE", variable=retrieve_var)
    checkbox_update = Checkbutton(subframe, text="UPDATE", variable=update_var)
    checkbox_delete = Checkbutton(subframe, text="DELETE", variable=delete_var)

    result_message = Message(subframe, textvariable=result_var)

    def callback():
        if create_var.get():
            check = checker.check_url(url_entry.get())

            if check == False:
                tkMessageBox.showinfo("ERROR", "Wrong URL")
            else:
                json_data = _retrieve_input(json_text)
                result_var.set(syntax_tester.test_syntax_response("create", url_entry.get(), json_data))
        if retrieve_var.get():
            check = checker.check_url(url_entry.get())

            if check == False:
                tkMessageBox.showinfo("ERROR", "Wrong URL")
            else:
                result_var.set(
                    syntax_tester.test_syntax_response("retrieve", url_entry.get()))
        if update_var.get():
            check = checker.check_url(url_entry.get())

            if check == False:
                tkMessageBox.showinfo("ERROR", "Wrong URL")
            else:
                json_data = _retrieve_input(json_text)
                result_var.set(syntax_tester.test_syntax_response("update", url_entry.get(), json_data))
        if delete_var.get():
            check = checker.check_url(url_entry.get())

            if check == False:
                tkMessageBox.showinfo("ERROR", "Wrong URL")
            else:
                result_var.set(syntax_tester.test_syntax_response("delete", url_entry.get()))

    button_send = Button(subframe, text="Test", command=callback)

    result_message.grid(row=6)
    button_send.grid(row=5, column=1)

    json_label.grid(row=2, column=0)
    json_text.grid(row=2, column=1)
    json_scrollb.grid(row=2, column=2, sticky='nsew')

    url_entry.grid(row=0, column=1)
    url_label.grid(row=0, column=0)

    checkbox_create.grid(row=3, column=0)
    checkbox_retrieve.grid(row=3, column=1)
    checkbox_update.grid(row=3, column=2)
    checkbox_delete.grid(row=3, column=3)


def create_custom_behaviour_frames(subframe, sender):
    behaviour_tests = bt.BehaviorTests(sender)

    result_var = StringVar()
    list_opts = [2, 3, 4, 5, 6, 7, 8, 9]
    list_var = StringVar()
    drop = OptionMenu(subframe, list_var, *list_opts)

    widgets, data, line = gui_helper.create_behaviour_frame(subframe, 2)

    def callback_test():
        d = gui_helper.create_behaviour_data(data)
        result_var.set(behaviour_tests._test_behaviour(d[0], d[1], d[2], d[3]))

    test_button = Button(subframe, text="Test", command=callback_test)
    result_message = Message(subframe, textvariable=result_var)

    def callback_apply():
        print(len(widgets))
        gui_helper.widgets_clear(widgets)
        _assign_behaviour_data(list_var.get(), widgets, data, line, subframe, test_button, callback_test)

    apply_button = Button(subframe, text="Apply", command=callback_apply)

    drop.grid(row=0, column=0)
    apply_button.grid(row=0, column=1)
    test_button.grid(row=line + 2)
    result_message.grid(row=line+3)


def _retrieve_input(text_box):
    json_data = text_box.get("1.0", END)

    try:
        json_data = json.loads(json_data)
    except:
        print("\n Test could not be run because the string is not a valid JSON String! \n")
        return {}

    return json_data


def _assign_behaviour_data(count, widgets, data, line, subframe, test_button, callback_test):
    widgets, data, line = gui_helper.create_behaviour_frame(subframe, int(count))
    test_button.grid_remove()

    test_button = Button(subframe, text="Test", command=callback_test)
    test_button.grid(row=line + 2)


def create_response_functional_frame(subframe, sender):
    parameter_functional_tests = rpt.ResponseParameterTests(sender)

    result_var = StringVar()

    url_label = Label(subframe, text="URL")

    url_entry = Entry(subframe, width=60)

    expected_parameter = Entry(subframe)
    expected_label = Label(subframe, text="Expected Parameter and Value")
    expected_value = Entry(subframe, width=20)

    result_message = Message(subframe, textvariable=result_var)

    def callback():
        check = checker.check_url(url_entry.get())

        if check == False:
            tkMessageBox.showinfo("ERROR", "Wrong URL")
        else:
            result_var.set(
                parameter_functional_tests.check_attribute_retrieve(url_entry.get(), expected_parameter.get(),
                                                                    expected_value.get()))

    button_send = Button(subframe, text="Test", command=callback)

    result_message.grid(row=6)
    button_send.grid(row=5, column=1)

    expected_parameter.grid(row=1, column=1)
    expected_value.grid(row=1, column=2)
    expected_label.grid(row=1, column=0)

    url_entry.grid(row=0, column=1)
    url_label.grid(row=0, column=0)
