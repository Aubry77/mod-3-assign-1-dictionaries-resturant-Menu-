def add_beverages(menu):
    """
    Add a new category called "Beverages" with at least two items to the restaurant menu.

    Args:
        menu (dict): The restaurant menu dictionary.

    Returns:
        None
    """
    menu["Beverages"] = {"Coffee": 2.99, "Tea": 2.49}

def update_steak_price(menu):
    """
    Update the price of "Steak" to 17.99 in the restaurant menu.

    Args:
        menu (dict): The restaurant menu dictionary.

    Returns:
        None
    """
    menu["Main Course"]["Steak"] = 17.99

def remove_bruschetta(menu):
    """
    Remove "Bruschetta" from the "Starters" category in the restaurant menu.

    Args:
        menu (dict): The restaurant menu dictionary.

    Returns:
        None
    """
    del menu["Starters"]["Bruschetta"]

def print_menu(menu):
    """
    Print the restaurant menu.

    Args:
        menu (dict): The restaurant menu dictionary.

    Returns:
        None
    """
    print(menu)

if __name__ == '__main__':
    restaurant_menu = {
        "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
        "Main Course": {"Steak": 15.99, "Salmon": 13.99},
        "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
    }

    add_beverages(restaurant_menu)
    update_steak_price(restaurant_menu)
    remove_bruschetta(restaurant_menu)
    print_menu(restaurant_menu)


if __name__ == '__main__':
    restaurant_menu = {
        "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
        "Main Course": {"Steak": 15.99, "Salmon": 13.99},
        "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}}

    add_beverages(restaurant_menu)
 
 
    update_steak_price(restaurant_menu)
    remove_bruschetta(restaurant_menu)
    print_menu(restaurant_menu)

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cre6am": 3.99}:
}
 
 # Initial sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(tickets, customer, issue):
    """
    Open a new service ticket.

    Args:
        tickets (dict): The dictionary of service tickets.
        customer (str): The name of the customer.
        issue (str): The issue description.

    Returns:
        None
    """
    ticket_id = f"Ticket{len(tickets) + 1:03d}"
    tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"New ticket opened: {ticket_id}")

def update_ticket_status(tickets, ticket_id, status):
    """
    Update the status of an existing ticket.

    Args:
        tickets (dict): The dictionary of service tickets.
        ticket_id (str): The ID of the ticket to update.
        status (str): The new status of the ticket.

    Returns:
        None
    """
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = status
        print(f"Ticket {ticket_id} status updated to {status}")
    else:
        print(f"Ticket {ticket_id} not found")

def display_tickets(tickets, status=None):
    """
    Display all tickets or filter by status.

    Args:
        tickets (dict): The dictionary of service tickets.
        status (str, optional): The status to filter by. Defaults to None.

    Returns:
        None
    """
    for ticket_id, details in tickets.items():
        if status is None or details["Status"] == status:
            print(f"{ticket_id}: {details}")

def main():
    """
    Main function to demonstrate the functionality of the customer service ticket tracker.

    Returns:
        None
    """
    # Open a new ticket
    open_ticket(service_tickets, "Charlie", "Network issue")
    
    # Update the status of an existing ticket
    update_ticket_status(service_tickets, "Ticket001", "closed")
    
    # Display all tickets
    print("\nAll tickets:")
    display_tickets(service_tickets)
    
    # Display only open tickets
    print("\nOpen tickets:")
    display_tickets(service_tickets, status="open")

if __name__ == '__main__':
    main()
