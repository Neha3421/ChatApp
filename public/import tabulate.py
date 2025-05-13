import tabulate

leads = []

def add_lead():
    name = input("Enter lead name: ")
    email = input("Enter email: ")
    status = "New"
    leads.append({"name": name, "email": email, "status": status})
    print("Lead added successfully!")

def update_lead_status():
    name = input("Enter lead name to update status: ")
    for lead in leads:
        if lead["name"].lower() == name.lower():
            print("Select new status: 1. Contacted  2. Converted")
            choice = input("Enter choice: ")
            if choice == "1":
                lead["status"] = "Contacted"
            elif choice == "2":
                lead["status"] = "Converted"
            else:
                print("Invalid choice!")
                return
            print("Lead status updated!")
            return
    print("Lead not found!")

def view_leads():
    if not leads:
        print("No leads available.")
        return
    print(tabulate.tabulate(leads, headers="keys", tablefmt="grid"))

def main():
    while True:
        print("\nLead Tracking System")
        print("1. Add Lead")
        print("2. Update Lead Status")
        print("3. View Leads")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_lead()
        elif choice == "2":
            update_lead_status()
        elif choice == "3":
            view_leads()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
