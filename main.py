from expense import Expense

expenses = []

#add expense
def add_expense():
    
    file = open("expenses.txt","a+")
    file.seek(0)
    
    data = file.readlines()
    
    expense_id = len(data) + 1
    
    file.close()
        
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    
    expense = Expense(expense_id,title, amount, category, date)   
    
    expenses.append(expense)
    
    file = open("expenses.txt","a")
    file.write(f"{expense.expense_id},{expense.title},{expense.amount},{expense.category},{expense.date}\n")
    file.close()
    
    print("\nExpense added succussfully!")

# view Expenses Function
def view_expenses():
    file = open("expenses.txt", "r")
    
    data = file.readlines()
    
    file.close()
    
    print("\n========== ALL EXPENSES ==========")
    
    for record in data:
        record = record.strip()
        
        expense_data = record.split(",")
        
        expense_id = expense_data[0]
        title = expense_data[1]
        amount = float(expense_data[2])
        category = expense_data[3]
        date = expense_data[4]
        
        print("\n-----------------------")
        print("ID:        ", expense_id)
        print("Title:     ", title)
        print("Amount:    ₹",amount)
        print("Category:  ", category)
        print("Date:      ", date)
        
    print("\n==============================")
    
# Search expense
def search_expense():
    search_id = input("Enter Expense ID to search: ")
    
    file = open("expenses.txt","r")
    data = file.readlines()
    file.close()
    
    found = False
    
    for record in data:
        record = record.strip()
        expense_data = record.split(",")
        
        expense_id = expense_data[0]
        
        if expense_id == search_id:
            found = True
        
            print("\n===== EXPENSE FOUND =====")
            print("ID:        ",expense_data[0])
            print("Title:     ",expense_data[1])
            print("Amount      ₹",float(expense_data[2]))
            print("Category:   ", expense_data[3])
            print("Date:       ", expense_data[4])
    
    if not found:
        print("Expense not found!")
        
# Update_expense
def update_expense():
    
    update_id = input("Enter Expense ID to update: ")
    
    file = open("expenses.txt","r")
    data = file.readlines()
    file.close()
    
    found = False
    
    updated_data = []
    
    for record in data:
        record = record.strip()
        expense_data = record.split(",")
        
        expense_id = expense_data[0]
        
        if expense_id == update_id:
            found = True
            
            print("\n==== ENTER NEW DETAILS  ====")
            
            title = input("Enter new title: ")
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ")
            date = input("Enter new date (YYYY-MM-DD): ")
            
            updated_record = f"{update_id},{title},{amount},{category},{date}"
            
            updated_data.append(updated_record)
            
        else:
            updated_data.append(record)
    
    if found:
        file = open("expenses.txt","w")
        
        for record in updated_data:
            file.write(record + "\n")
            
        file.close()
            
        print("\nExpense update successfully!")
    else:
        print("\nExpense not found!") 
        
#delete expense
def delete_expense():
    
    delete_id = input("Enter Expense ID to delete: ")
    
    file = open("expenses.txt","r")
    data = file.readlines()
    file.close()
    
    found = False
    
    remaining_data =[]
    
    for record in data:
        record = record.strip()
        expense_data = record.split(",")
        expense_id = expense_data[0]
        
        if expense_id == delete_id:
            found = True
        else:
            remaining_data.append(record)
            
    if found:
        file = open("expenses.txt", "w")
        
        new_id = 1
        
        for record in remaining_data:
            expense_data = record.split(",")
            
            expense_data[0] = str(new_id)
            
            updated_record = ",".join(expense_data)
            
            file.write(record + "\n")
            
            new_id += 1
            
        file.close()
        
        print("Expense deleted successfully!")
    
    else:
        print("Expense not found!")
            
        
while True: 
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()
    
    elif choice == "3":
        search_expense()
    
    elif choice == "4":
        update_expense()
    
    elif choice == "5":
        delete_expense()
        
    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break
    
    else:
        print("Invalid choice! Please try again.")