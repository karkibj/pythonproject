import json
import tkinter as tk
from tkinter import messagebox
from colorama import Fore
def main():
    deposit_withdraw_frame.pack_forget()
    create_in_frame.pack_forget()
    password_entry.delete(0,tk.END)
    # Reset the main window to its initial state
    sign_in_frame.pack(padx=40, pady=40)
    label_acnumber.pack()
    entry_acnumber.pack()
    label_pass.pack()
    password_entry.pack()
    checkBox_showPassword.pack(padx=10,pady=10)
    
    
    sign_in.pack(padx=20,pady=20)
    new_ac.pack()
    
    button_deposit.pack_forget()
    button_withdraw.pack_forget()
    button_check.pack_forget()
    result_text.set("")
    balance_text.set("")


class Bankaccount:
    
    Bankname = "LOOT BANK"
    Branch = 'Bhaktapur'
 
    def __init__(self, id, name:str, balance):
        self.ac_id = id
        self.ac_name = name
        self.balance = balance

    def perform_deposit(self, amount):
        
        self.balance = float(self.balance) + float(amount)

        # To Update the JSON file with the latest balance
        with open('LOOT_MEMBERS.json', 'r') as file:
            accounts_data = json.load(file)

        # Locate the account entry in the dictionary
        if self.ac_id in accounts_data:
            accounts_data[self.ac_id]['balance'] = self.balance

        # Write the updated dictionary back to the JSON file
        with open('LOOT_MEMBERS.json', 'w') as file:
            json.dump(accounts_data, file, indent=6, separators=(",", ": "))

        # Display the updated balance in the GUI
        balance_text.set(f"Your total amount: {self.balance}")
        result_text.set(f"You deposited: {amount}\nYour total amount: {self.balance}")
        

    def perform_withdraw(self, amount:int):
        if int(amount) > self.balance:
            result_text.set("You do not have enough balance")
        else:
            self.balance = float(self.balance) - float(amount)

        # Update the JSON file with the latest balance
        with open('LOOT_MEMBERS.json', 'r') as file:
            accounts_data = json.load(file)

        # Locate the account entry in the dictionary
        if self.ac_id in accounts_data:
            accounts_data[self.ac_id]['balance'] = self.balance

        # Write the updated dictionary back to the JSON file
        with open('LOOT_MEMBERS.json', 'w') as file:
            json.dump(accounts_data, file, indent=6, separators=(",", ": "))

           
            result_text.set(f"You withdrew: {amount}")
            balance_text.set(f"Your total amount: {self.balance}")

    def display(self):
        result_text.set(f"Bank Name: {self.Bankname}\n"
                        f"Branch: {self.Branch}\n"
                        f"Account Number: {self.ac_id}\n"
                        f"Account Holder: {self.ac_name}\n"
                        f"Balance: Rs. {self.balance}")


def create_account_number(accounts):
    if not accounts:
        return "208001"
    
    highest_ac_number = max(accounts.keys()) 
    new_ac_number = str(int(highest_ac_number) + 1)   

    return new_ac_number
    



def welcome_msg(name, acnumber):
    result_text.set(f"Dear {name}, your account has been created successfully\n"
                    f"Your new account number is: {acnumber}")
    label_result.config(fg="green",font=("Times New Roman",15))
    


def account_operations():
    button_deposit.pack(padx=5,pady=5)
    button_withdraw.pack(padx=10,pady=5)
    button_check.pack(padx=15,pady=5)


global_var=None
ac_number=None
ac_name=None



def create_new_ac():
    destroy()
    create_in_frame.pack()
    new_ac.pack_forget()
    new_name.pack()
    new_entry_name.pack()
    new_password.pack()
    new_entry_password.pack()
    checkBox_showPassword1.pack()



    def generate_account():
        
        with open('LOOT_MEMBERS.json','r') as f:
            account=json.load(f)
        global ac_number
        global ac_name
        
        ac_password=new_entry_password.get()
        ac_name=new_entry_name.get()
            

        ac_number = create_account_number(account)

        account[ac_number] = {"name": ac_name, "balance": balance,"Password":ac_password}
        accounts_data = {}
        for account_number, account_data in account.items():
            accounts_data[account_number] = account_data

        # Write the entire dictionary to the file with proper indentation
        with open("LOOT_MEMBERS.json", "w") as file:
            json.dump(accounts_data, file, indent=6, separators=(",", ": "))
                    # file.write("\n") 


        create.pack_forget()
        new_name.pack_forget()
        new_entry_name.pack_forget()
        password_entry.pack_forget()
        new_password.pack_forget()
        new_entry_password.pack_forget()
        checkBox_showPassword.pack_forget()
        create_in_frame.pack_forget()
        
            
    create.config(text="Create",command=lambda:[generate_account(),welcome_msg(name=ac_name,acnumber=ac_number)])
    create.pack() 
    balance = 0


 

#To remove widgets and labels
def destroy():
    sign_in_frame.pack_forget()
    entry_acnumber.delete(0,tk.END)
    password_entry.delete(0,tk.END)
    label_acnumber.pack_forget()
    label_pass.pack_forget()
    entry_acnumber.pack_forget()
    password_entry.pack_forget()
    sign_in.pack_forget()
    checkBox_showPassword.pack_forget()
    new_ac.pack_forget()



        
#Main program to take user's input
    
def take_input():
    with open("LOOT_MEMBERS.json", 'r') as file:
        accounts = json.load(file)

    acnumber = entry_acnumber.get()
    password= password_entry.get()


    accounts_exist = False
    if acnumber in accounts:
        
        accounts_exist = True
        rightpassword=accounts[acnumber]['Password']
        if password==rightpassword:
            messagebox.showinfo("Login Successful", "You have successfully logged in!")
            name = accounts[acnumber]['name']
            balance = accounts[acnumber]['balance']
            global global_var
            global_var = Bankaccount(acnumber, name, balance)
            destroy()
            global_var.display()
            account_operations()

        else:
            attempt_authorized = True
            messagebox.showerror("Invalid Input!!", " Please provide correct password") 
            password_entry.delete(0, tk.END)
            print(password_entry.get())
        
        
    else:
        
        accounts_exist = False
        result_text.set("Account does not exist!")
        label_result.config(fg="red",font=("Times New Roman",10))

        
        entry_acnumber.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        
        response = messagebox.askyesno("Account Not Found", "Account does not exist. Do you want to create a new account?")
        
        if response:
            create_new_ac()
        

def deposit():
    


    def perform():
        amount = amount_entry.get()
        
        
        global_var.perform_deposit(amount)

        deposit_withdraw_frame.pack_forget()
        amount_entry.pack_forget()
        amount_label.pack_forget()
        deposit_button.pack_forget()



    deposit_withdraw_frame.pack(padx=10,pady=10)
    amount_label.pack()
    amount_entry.pack()
    deposit_button = tk.Button(deposit_withdraw_frame, text="Deposit", command=perform)
    deposit_button.pack(padx=10,pady=5)
    
      


def withdraw():
    amount_label.pack_forget()
    amount_entry.pack_forget()
    global global_var

   

    def perform():
        amount = withdraw_entry.get()    
        global_var.perform_withdraw(amount)

        deposit_withdraw_frame.pack_forget()
                              # Remove the amount_entry widget



    deposit_withdraw_frame.pack()
    withdraw_label.pack()
    withdraw_entry.pack()
    withdraw_button = tk.Button(deposit_withdraw_frame, text="Withdraw", command=perform)
    withdraw_button.pack()
    



def display():
    deposit_withdraw_frame.pack_forget()
    global global_var
    global_var.display()

def show_and_hide():

    if password_entry['show']=='*':
        password_entry['show']=''
    else:
        password_entry['show']='*'


window = tk.Tk()

window.maxsize(600, 700)
window.title("Banking System")
window.geometry('600x700')

# Add background and bank name label
label = tk.Label(text="L∞T BANK", font=("Impact", 60), fg='white', bg='navy', bd=10, relief=tk.RAISED)
label.config(compound='center')
label.pack(padx=30, pady=30)

# Adding the description/slogan label below the main bank name label
title_bank = tk.Label(window, text="**Safeguarding Your Wealth, Empowering Your Future**", fg="green", font=('Comic Sans Ms', 12,'bold'))
title_bank.pack()

# Adding the description/slogan label below the main bank name label
description_label = tk.Label(window, text="-YOUR TRUSTED BANKING PARTNER-", fg="navy", font=('Arial', 11, 'bold'))
description_label.pack()

Home_button=tk.Button(window,text="Home",command=main,fg="black",relief=tk.RAISED)
Home_button.pack(padx=4)






# Create sign-in frame
sign_in_frame = tk.LabelFrame(window, text="Sign In", padx=20, pady=20)
sign_in_frame.pack(padx=40, pady=40)

# Create labels and entry fields inside the sign-in frame
label_acnumber = tk.Label(sign_in_frame, text="Account Number:")
label_acnumber.pack()

entry_acnumber = tk.Entry(sign_in_frame)
entry_acnumber.pack()

label_pass = tk.Label(sign_in_frame, text="Password:")
label_pass.pack()

password_entry = tk.Entry(sign_in_frame, show="*")
password_entry.pack()

checkBox_showPassword = tk.Checkbutton(sign_in_frame, text="Show", bg='#ddd', fg='red', font=('verdana', 10), command=show_and_hide)
checkBox_showPassword.pack(padx=10, pady=10)

# Create sign-in button
sign_in = tk.Button(sign_in_frame, text="Sign In", bg="green", command=take_input)
sign_in.pack(padx=20, pady=20)

# Create a button for creating a new account
new_ac = tk.Button(window, text="Create account", fg='blue',command=create_new_ac)
new_ac.pack()

# Create buttons (hidden initially)
button_deposit = tk.Button(window, text="Deposit", command=deposit,fg='green')
button_withdraw = tk.Button(window, text="Withdraw", command=withdraw,fg='red')
button_check = tk.Button(window, text="Check Account", command=display,fg='sky blue')



#frame for deposit and entry:
deposit_withdraw_frame=tk.LabelFrame(window,text="Enter amount",)
amount_label = tk.Label(deposit_withdraw_frame, text="Enter amount")
amount_entry = tk.Entry(deposit_withdraw_frame)  
withdraw_label=tk.Label(deposit_withdraw_frame,text="Enter amount")
withdraw_entry=tk.Entry(deposit_withdraw_frame)


#For new account frame
create_in_frame = tk.LabelFrame(window, text="Create Account", padx=20, pady=20)
create_in_frame.pack(padx=40, pady=40)

new_name=tk.Label(create_in_frame,text="Name:")
new_entry_name=tk.Entry(create_in_frame)
new_password=tk.Label(create_in_frame,text="Password:")
new_entry_password=tk.Entry(create_in_frame,show="*")
create=tk.Button(create_in_frame)
checkBox_showPassword1 = tk.Checkbutton(create_in_frame, text="Show", bg='#ddd', fg='red', font=('verdana', 10), command=show_and_hide)



#at the button
founder = tk.Label(window, text="DEVELOPED BY: BIZAY KARKI", font=("Arial", 10,'italic'), fg="black")
founder.pack(side=tk.BOTTOM)









# Create result and balance labels
result_text = tk.StringVar()
label_result = tk.Label(window, textvariable=result_text)
label_result.pack()

balance_text = tk.StringVar()



# Run the GUI event loop
window.mainloop()


