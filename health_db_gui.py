import tkinter as tk
from tkinter import ttk
# from health_db_client import add_patient_to_server

def create_output(name, id, blood_letter, rh_factor, center):
    out_string = "Patient name: {}\n".format(name)
    out_string+= "Blood type: {}\n".format(blood_letter)
    out_string+= "Donation Center{}\n".format(center)
    answer = add_patient_to_server(name, id, "{}{}".format(blood_letter,rh_factor))
    return out_string, answer

def design_window():

    def ok_button_cmd():
        # Get needed data from GUI
        name = name_data.get()
        id = id_data.get()
        blood_letter = blood_letter_data.get()
        rh_factor = rh_data.get()
        center = donation_center_data.get()
        # Call external function to do the work that can be tested
        answer = create_output(name, id, blood_letter, rh_factor, center)
        # Update GUI
        print(answer)
        output_string.configure(text=answer)

    def cancel_button_cmd():
        root.destroy()



    root = tk.Tk()
    root.title("Health Database GUI")
    # root.geometry("1000x200")
    # root.configure(bg='blue')

    frame = tk.Frame(root, bg="white")
    frame.pack()

    top_label = ttk.Label(frame, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sticky='w')

    ttk.Label(frame, text="Name").grid(column=0, row=1)

    name_data = tk.StringVar()
    name_entry_box = ttk.Entry(frame, width=50, textvariable=name_data)
    name_entry_box.grid(column=1, row=1, sticky='w', columnspan=2)

    ttk.Label(frame, text="ID").grid(column=0, row=2)

    id_data = tk.StringVar()
    id_entry_box = ttk.Entry(frame, width=10, textvariable=id_data)
    id_entry_box.grid(column=1, row=2, sticky='w', padx=20, pady=20)

    blood_letter_data = tk.StringVar()
    ttk.Radiobutton(frame, text="A", variable=blood_letter_data,
                    value="A").grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(frame, text="B", variable=blood_letter_data,
                    value="B").grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(frame, text="AB", variable=blood_letter_data,
                    value="AB").grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(frame, text="O", variable=blood_letter_data,
                    value="O").grid(column=0, row=6, sticky=tk.W)

    rh_data = tk.StringVar()
    rh_data.set('-')
    rh_checkbox = ttk.Checkbutton(frame, text="Rh Positive", variable=rh_data, onvalue = "+", offvalue="-")
    rh_checkbox.grid(column=1, row=4)

    ttk.Label(root, text="Nearest Donation Center").grid(column=2, row=0)
    donation_center_data = tk.StringVar()
    combo_box = ttk.Combobox(root, textvariable=donation_center_data)
    combo_box["values"] = ("Durham", "Raleigh", "Cary", "Apex")
    combo_box.state(["readonly"])
    combo_box.grid(column=3, row=1)

    output_string = ttk.Label()
    output_string.grid(column=1, row=10)

    ok_button = ttk.Button(frame, text="Ok", command=ok_button_cmd)
    ok_button.grid(column=1, row=6)

    cancel_button = ttk.Button(frame, text="Cancel", command=cancel_button_cmd)
    cancel_button.grid(column=2, row=6)

    root.mainloop()


if __name__ == "__main__":
    design_window()