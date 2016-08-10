""" 

Some Helper functions for the GUI

"""

try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import json


def add_scroll(container):
    canvas = Canvas(container, width=1200, height=450)
    scroll = Scrollbar(container, command=canvas.yview)
    canvas.config(yscrollcommand=scroll.set, scrollregion=(0, 0, 100, 1000))
    scroll.pack(side=RIGHT, fill=Y)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    sub = Frame(canvas)
    sub_id = canvas.create_window(0, 0, window=sub, anchor=NW)

    # track changes to the canvas and frame width and sync them,
    # also updating the scrollbar
    def _configure_sub(event):
        # update the scrollbars to match the size of the inner frame
        size = (sub.winfo_reqwidth(), sub.winfo_reqheight())
        canvas.config(scrollregion="0 0 %s %s" % size)
        if sub.winfo_reqwidth() != canvas.winfo_width():
            # update the canvas's width to fit the inner frame
            canvas.config(width=sub.winfo_reqwidth())

    sub.bind('<Configure>', _configure_sub)

    def _configure_canvas(event):
        if sub.winfo_reqwidth() != canvas.winfo_width():
            # update the inner frame's width to fill the canvas
            canvas.itemconfigure(sub_id, width=canvas.winfo_width())

    canvas.bind('<Configure>', _configure_canvas)

    return sub


def create_behaviour_frame(subframe, count):
    url_entries = list()
    exp_entries = list()
    json_entries = list()
    create_checks = [None] * count
    delete_checks = [None] * count
    retrieve_checks = [None] * count
    update_checks = [None] * count

    widgets = list()

    line = 1

    for i in range(0, count):
        create_checks[i] = BooleanVar()
        retrieve_checks[i] = BooleanVar()
        update_checks[i] = BooleanVar()
        delete_checks[i] = BooleanVar()

        url_label = Label(subframe, text="URL")
        url_entry = Entry(subframe, width=60)

        expected_entry = Entry(subframe)
        expected_label = Label(subframe, text="Expected Response Status")

        json_text = Text(subframe, width=60, height=12)
        json_label = Label(subframe, text="JSON (if needed)")

        json_scrollb = Scrollbar(subframe, command=json_text.yview)
        json_text['yscrollcommand'] = json_scrollb.set

        checkbox_create = Checkbutton(subframe, text="CREATE", variable=create_checks[i])
        checkbox_retrieve = Checkbutton(subframe, text="RETRIEVE", variable=retrieve_checks[i])
        checkbox_update = Checkbutton(subframe, text="UPDATE", variable=update_checks[i])
        checkbox_delete = Checkbutton(subframe, text="DELETE", variable=delete_checks[i])

        json_label.grid(row=line + 2, column=0)
        json_text.grid(row=line + 2, column=1)
        json_scrollb.grid(row=line + 2, column=2, sticky='nsew')

        expected_entry.grid(row=line + 1, column=1)
        expected_label.grid(row=line + 1, column=0)

        url_entry.grid(row=line + 0, column=1)
        url_label.grid(row=line + 0, column=0)

        checkbox_create.grid(row=line + 3, column=0)
        checkbox_retrieve.grid(row=line + 3, column=1)
        checkbox_update.grid(row=line + 3, column=2)
        checkbox_delete.grid(row=line + 3, column=3)

        widgets.append(url_label)
        widgets.append(url_entry)
        widgets.append(expected_label)
        widgets.append(expected_entry)
        widgets.append(json_label)
        widgets.append(json_text)
        widgets.append(json_scrollb)
        widgets.append(checkbox_create)
        widgets.append(checkbox_retrieve)
        widgets.append(checkbox_delete)
        widgets.append(checkbox_update)

        json_entries.append(json_text)
        exp_entries.append(expected_entry)
        url_entries.append(url_entry)

        line += 8

    data = list()
    data.append(url_entries)
    data.append(exp_entries)
    data.append(json_entries)
    data.append(create_checks)
    data.append(retrieve_checks)
    data.append(update_checks)
    data.append(delete_checks)

    return widgets, data, line


def create_behaviour_data(data):
    url_entries = data[0]
    exp_entries = data[1]
    json_entries = data[2]
    create_vars = data[3]
    get_vars = data[4]
    update_vars = data[5]
    delete_vars = data[6]

    urls = list()
    exps = list()
    jsons = list()
    methods = list()

    for i in range(0, len(url_entries)):
        url = url_entries[i].get()
        exp = exp_entries[i].get()
        json_data = _retrieve_input(json_entries[i])
        create_var = create_vars[i]
        retrieve_var = get_vars[i]
        update_var = update_vars[i]
        delete_var = delete_vars[i]
        method = ""

        if create_var.get():
            method = "create"
        if retrieve_var.get():
            method = "get"
        if update_var.get():
            method = "update"
        if delete_var.get():
            method = "delete"

        urls.append(url)
        exps.append(exp)
        jsons.append(json_data)
        methods.append(method)

    print(urls)
    print(jsons)
    print(methods)
    print(exps)
    return urls, jsons, methods, exps


def widgets_clear(widgets):
    for widget in widgets:
        widget.grid_remove()

    widgets = list()


def _retrieve_input(text_box):
    json_data = text_box.get("1.0", END)

    try:
        json_data = json.loads(json_data)
    except:
        # print("\n Test could not be run because the string is not a valid JSON String! \n")
        return {}

    return json_data
