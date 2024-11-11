import tkinter as tk
import os
import sys
import json
from tkinter import messagebox

#Lägg till på page3, en ruta är man kan skriva planerat implemmenteringsdatum, när det är skriver så ska även listan uppdateras med Namn, info och -datumet-
#fixa search-rutan så att den faktiskt funkar

STATE_FILE = "app_state.json"
def save_state(): #save current state of app
    available_pcs = []
    for i in range(available_pcs_list.size()):
        pc_entry = available_pcs_list.get(i)
        pc_name = pc_entry.split("|")[0].strip()  #extract the PC name        
        pc_info = available_pcs_details.get(pc_name, {}) #Retrieve additional info from the dictionary
        pc_data = {
            "name": pc_name,
            "owner": pc_info.get("owner", ""),
            "date_added": pc_info.get("date_added", ""),
            "last_serviced": pc_info.get("last_serviced", ""),
            "display_text": pc_entry  #Save the display text of the item
        }
        available_pcs.append(pc_data)

    service_pcs = []
    for i in range(service_pcs_list.size()):
        pc_entry = service_pcs_list.get(i)
        pc_name = pc_entry.split("|")[0].strip()
        pc_info = available_pcs_details.get(pc_name, {})
        pc_data = {
            "name": pc_name,
            "owner": pc_info.get("owner", ""),
            "date_added": pc_info.get("date_added", ""),
            "last_serviced": pc_info.get("last_serviced", ""),
            "display_text": pc_entry
        }
        service_pcs.append(pc_data)

    state = {
        "available_pcs": available_pcs,
        "service_pcs": service_pcs,
        "window_position": f"{window.winfo_x()},{window.winfo_y()}"
    }
    with open(STATE_FILE, "w") as file:
        json.dump(state, file)

def load_state(): #load saved state
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as file:
            state = json.load(file)
            
            available_pcs = state.get("available_pcs", [])
            for pc_data in available_pcs:
                pc_name = pc_data.get("name", "")
                owner = pc_data.get("owner", "")
                date_added = pc_data.get("date_added", "")
                last_serviced = pc_data.get("last_serviced", "")
                display_text = pc_data.get("display_text", "")
                available_pcs_list.insert(tk.END, display_text)
                available_pcs_details[pc_name] = {
                    "owner": owner,
                    "date_added": date_added,
                    "last_serviced": last_serviced
                }

            service_pcs = state.get("service_pcs", [])
            for pc_data in service_pcs:
                pc_name = pc_data.get("name", "")
                owner = pc_data.get("owner", "")
                date_added = pc_data.get("date_added", "")
                last_serviced = pc_data.get("last_serviced", "")
                display_text = pc_data.get("display_text", "")

                service_pcs_list.insert(tk.END, display_text)
                available_pcs_details[pc_name] = {
                    "owner": owner,
                    "date_added": date_added,
                    "last_serviced": last_serviced
                }
            #Restore window position
            position = state.get("window_position", "100,100")
            x, y = position.split(",")
            window.geometry(f"+{x}+{y}")

def on_closing():
    # Ask the user for confirmation before closing
    if messagebox.askokcancel("Quit", "Do you want to save and exit?"):
        save_state()  #save data
        window.destroy()

def refresh_app():
    save_state()
    python = sys.executable
    script = r"C:\IT\Programmering 1\Python_arbeten\computer_management_with_tkinter.py"
    os.execl(python, f'"{python}"', f'"{script}"')



#----------------------------------------------------------------------------------------------



def show_frame(frame):
    frame.tkraise()

window = tk.Tk() #Creates the app itself
window.title("Computer Management") #apprubriken
window.geometry("800x600") #storleken på appen

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

page1 = tk.Frame(window) #Sida 1, Start page
page2 = tk.Frame(window) #Sida 2, Available pcs page
page3 = tk.Frame(window) #Sida 3, Service pcs page

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky="nsew")

#Page 1 contents
label1 = tk.Label(page1,text="Choose action", font=("System", 20))
label1.place(relx=0.5, rely=0.3, anchor="center")
button_to_available_pcs = tk.Button(page1, text="Available Computers", font=("System", 8), 
                            command=lambda: show_frame(page2)) #Goes to page 2
button_to_available_pcs.place(relx=0.4, rely=0.4, anchor="center")

button__to_pcs_on_service = tk.Button(page1, text="Computers on Service", font=("System", 8), 
                         command=lambda: show_frame(page3)) #Goes to page 3
button__to_pcs_on_service.place(relx=0.6, rely=0.4, anchor="center")

#Page 2 contents
label2 = tk.Label(page2, text="Available Computers", font=("System", 20))
label2.pack(pady=20)
available_pcs_list = tk.Listbox(page2, font=("System", 8))
available_pcs_list.place(relx=0.045, rely=0.6, relwidth=0.9, relheight=0.3)

button_to_page1 = tk.Button(page2, text="Back", font=("System", 8),
                            command=lambda: [available_pcs_list.selection_clear(0, tk.END),information_button_page1.place_forget(), page2_remove_button.place_forget(),send_to_service_button.place_forget(), pc_name_entry.focus_set(), show_frame(page1)])
button_to_page1.pack()

pc_name_entry = tk.Entry(page2)
pc_name_entry.place(relx=0.045, rely=0.5, relwidth=0.2)
pc_additional_info_entry = tk.Entry(page2)
pc_additional_info_entry.place (relx=0.265, rely=0.5, relwidth=0.35)
pc_name_label = tk.Label(page2, text="*Computer name:",fg="gray", font=("System", 5))
pc_name_label.place(relx=0.045, rely=0.46)
pc_info_label = tk.Label(page2, text="Additional info:",fg="gray", font=("System", 5))
pc_info_label.place(relx=0.265, rely=0.46)

page2_pc_search_label = tk.Label(page2, text="Search:", fg="gray", font=("System", 8))
page2_pc_search_label.place(relx=0.738, rely=0.497)
available_pc_search_entry = tk.Entry(page2)
available_pc_search_entry.place(relx=0.815, rely=0.5, relwidth=0.13)
divider_page2_label = tk.Label(page2, text="|", font=("System", 15), fg="gray")
divider_page2_label.place(relx=0.72, rely=0.49)

def add_pc_to_list():
    pc_name = pc_name_entry.get()
    pc_additional_info = pc_additional_info_entry.get()

    def display_message(message, color):
        message_label.config(text=message, fg=color)
        frame.after(5000, clear_message)  #clear message after 5 seconds

    def clear_message():
        message_label.config(text="")

    if not pc_name:
        display_message("Please fill out all required fields!", "red")
        return

    pc_entry = f"  {pc_name}   |   Info: {pc_additional_info}"
    available_pcs_list.insert(tk.END, pc_entry)

    pc_name_entry.delete(0, tk.END)
    pc_additional_info_entry.delete(0, tk.END)

def remove_selected():
    selected_items = available_pcs_list.curselection() #removes highlighted

    def display_message2(message, color):
        message_label2.config(text=message, fg=color)
        frame.after(5000, clear_message)

    def clear_message():
        message_label2.config(text="")

    if not selected_items:
        display_message2("Please select the computer you want to remove.", "red")
        return
    for index in reversed(selected_items):
        available_pcs_list.delete(index)

def toggle_remove_button(event):
    if available_pcs_list.curselection():
        page2_remove_button.place(relx=0.045, rely=0.925)  #show button
   
    else:
        page2_remove_button.place_forget()  #hide button
   
def toggle_send_to_service_button(event):
    if available_pcs_list.curselection():
        send_to_service_button.place(relx=0.795, rely=0.925, relwidth=0.15)
    else:
        send_to_service_button.place_forget()

def move_to_service_page3 ():
    selected_item = available_pcs_list.curselection()

    if selected_item:
        selected_text = available_pcs_list.get(selected_item) #pc selected in available list
        service_pcs_list.insert(tk.END, selected_text) #put selected pc in service list
        available_pcs_list.delete(selected_item) #delete from available list

def toggle_information_button_page2(event):
    if available_pcs_list.curselection():
        information_button_page1.place(relx=0.42, rely=0.925)
    else:
        information_button_page1.place_forget()

add_pc_button = tk.Button(page2, text="Add", font=("System", 8), command=add_pc_to_list)
add_pc_button.place(relx=0.622, rely=0.49, relwidth=0.095)

page2_remove_button = tk.Button(page2, text="Remove",fg="red", font=("System", 8), command=remove_selected)
send_to_service_button = tk.Button (page2, text="Move to service", font=("System", 8), command=move_to_service_page3)

def on_listbox_select(event):
    toggle_remove_button(event)
    toggle_send_to_service_button(event)
    toggle_information_button_page2(event)
available_pcs_list.bind("<<ListboxSelect>>", on_listbox_select)

message_label = tk.Label(page2, text="", font=("System", 7))
message_label.place(relx=0.365, rely=0.4)
message_label2 = tk.Label(page2, text="", font=("System", 7))
message_label2.place(relx=0.15, rely=0.930)

available_pcs_details = {}

def show_information_window():
    selected_item = available_pcs_list.curselection()
    selected_index = selected_item[0]
    selected_text = available_pcs_list.get(selected_index)

    pc_name = selected_text.split("|")[0].strip()
    pc_details = available_pcs_details.get(pc_name, {
        "owner": "",
        "date_added": "",
        "last_serviced": "",
    })

    info_window = tk.Toplevel(window)
    info_window.title(f"Information for {pc_name}")
    info_window.geometry("300x250")

    #Owner entry
    tk.Label(info_window, text="Owner:").pack(pady=5)
    owner_entry = tk.Entry(info_window)
    owner_entry.pack()
    owner_entry.insert(0, pc_details.get("owner", ""))

    #Date Added entry
    tk.Label(info_window, text="Date Added (YYYY-MM-DD):").pack(pady=5)
    date_added_entry = tk.Entry(info_window)
    date_added_entry.pack()
    date_added_entry.insert(0, pc_details.get("date_added", ""))

    #Last Serviced entry
    tk.Label(info_window, text="Last Serviced (YYYY-MM-DD):").pack(pady=5)
    last_serviced_entry = tk.Entry(info_window)
    last_serviced_entry.pack()
    last_serviced_entry.insert(0, pc_details.get("last_serviced", ""))

    def save_information():
        owner = owner_entry.get()
        date_added = date_added_entry.get()
        last_serviced = last_serviced_entry.get()

        available_pcs_details[pc_name] = {
            "owner": owner,
            "date_added": date_added,
            "last_serviced": last_serviced
        }
        save_state()
        messagebox.showinfo("Success", "Information saved")
        info_window.destroy()
        
    save_info_button = tk.Button(info_window, text="Save", command=save_information)
    save_info_button.pack(pady=20)

information_button_page1 = tk.Button(page2, text="Information", font=("System", 8), fg="green", command=show_information_window)
information_button_page1.place()

#Page 3 Contents
label3 = tk.Label(page3, text="Computers on Service", font=("System", 20))
label3.pack(pady=20)
button_to_page1 = tk.Button(page3, text="Back", font=("System", 8), 
                            command=lambda: [service_pcs_list.selection_clear(0, tk.END),page3_remove_button.place_forget(),send_to_availablepcs_button.place_forget(),service_pc_name_entry.focus_set(),show_frame(page1)])
button_to_page1.pack()

service_pcs_list = tk.Listbox(page3, font=("System", 8))
service_pcs_list.place(relx=0.045, rely=0.6, relwidth=0.9, relheight=0.3)

page3_pc_search_label = tk.Label(page3, text="Search:", fg="gray", font=("System", 8))
page3_pc_search_label.place(relx=0.738, rely=0.497)
service_pc_search_entry = tk.Entry(page3)
service_pc_search_entry.place(relx=0.815, rely=0.5, relwidth=0.13)
divider_page3_label = tk.Label(page3, text="|", font=("System", 15), fg="gray")
divider_page3_label.place(relx=0.72, rely=0.49)

service_pc_name_entry = tk.Entry(page3)
service_pc_name_entry.place(relx=0.045, rely=0.5, relwidth=0.2)
service_additional_info_entry = tk.Entry(page3)
service_additional_info_entry.place(relx=0.265, rely=0.5, relwidth=0.35)
service_name_page3_label = tk.Label(page3, text="*Computer name:", font=("System", 5), fg="gray")
service_name_page3_label.place(relx=0.045, rely=0.46)
service_additionalinfo_page3_label = tk.Label(page3, text="Additional info:", font=("System", 5), fg="gray")
service_additionalinfo_page3_label.place(relx=0.265, rely=0.46)

def add_service_pc_to_list():
    service_pc_name = service_pc_name_entry.get()
    service_pc_additional_info = service_additional_info_entry.get()

    def page3_display_message(message, color):
        message_label3.config(text=message, fg=color)
        frame.after(5000, clear_message)

    def clear_message():
        message_label3.config(text="")

    if not service_pc_name:
        page3_display_message("Please fill out all required fields!", "red")
        return
    
    service_pc_entry = f"  {service_pc_name}   |   Info: {service_pc_additional_info}"
    service_pcs_list.insert(tk.END, service_pc_entry)

    service_pc_name_entry.delete(0, tk.END)
    service_additional_info_entry.delete(0, tk.END)

message_label3 = tk.Label(page3, text="", font=("System", 7))
message_label3.place(relx=0.365, rely=0.4)

def service_remove_selected():
    selected_items = service_pcs_list.curselection()

    def display_message4(message, color):
        message_label4.config(text=message, fg=color)
        frame.after(5000, service_clear_message)

    def service_clear_message():
        message_label4.config(text="")

    if not selected_items:
        display_message4("Please select the computer you want to remove.", "red")
        return
    for index in reversed(selected_items):
        service_pcs_list.delete(index)

def service_toggle_remove_button(event):
    if service_pcs_list.curselection():
        page3_remove_button.place(relx=0.045, rely=0.925)
   
    else:
        page3_remove_button.place_forget()
   
def toggle_send_to_availablepcs_button(event):
    if service_pcs_list.curselection():
        send_to_availablepcs_button.place(relx=0.795, rely=0.925, relwidth=0.15)
    else:
        send_to_availablepcs_button.place_forget()

#def service_toggle_pc_information_button(event):
    #if service_pcs_list.curselection():
        #service_information_button.place(relx=0.42, rely=0.925)
    #else:
        #service_information_button.place_forget()

message_label4 = tk.Label(page3, text="", font=("System", 7))
message_label4.place(relx=0.365, rely=0.4)

page3_remove_button = tk.Button(page3, text="Remove",fg="red", font=("System", 8), command=service_remove_selected)

def move_pc_to_available_page2 ():
    selected_item = service_pcs_list.curselection()

    if selected_item:
        selected_text = service_pcs_list.get(selected_item) #get the text from service list
        available_pcs_list.insert(tk.END, selected_text) #insert the text in available list
        service_pcs_list.delete(selected_item) #delete from service list
send_to_availablepcs_button = tk.Button (page3, text="Make Available", font=("System", 8), command=move_pc_to_available_page2)

#service_information_button = tk.Button(page3, text="Information", fg="green", font=("System", 8), 
                                       #command=lambda: show_information_window(service_pcs_list))
service_add_button = tk.Button(page3, text="Add", font=("System", 8), command=add_service_pc_to_list)
service_add_button.place(relx=0.622, rely=0.49, relwidth=0.095)

def on_service_listbox_select(event):
    service_toggle_remove_button(event)
    toggle_send_to_availablepcs_button(event)
    #service_toggle_pc_information_button(event)
service_pcs_list.bind("<<ListboxSelect>>", on_service_listbox_select)

load_state()

#refresh button on page 1
refresh_button = tk.Button(page1, fg="blue", text="Refresh App", command=refresh_app)
refresh_button.place(relx=0.795, rely=0.055, relwidth=0.15)

#show first page initially
show_frame(page1)

#bind the on_closing function to the window close event (the "X" button)
window.protocol("WM_DELETE_WINDOW", on_closing)

#makes the app visible
window.mainloop()
