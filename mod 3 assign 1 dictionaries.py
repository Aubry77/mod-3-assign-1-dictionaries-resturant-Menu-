"""
Module for updating a restaurant menu and tracking customer service tickets.
"""

def update_menu(menu):
    """
    Update the restaurant menu.
    
    Args:
        menu (dict): The initial restaurant menu.
    
    Returns:
        dict: The updated restaurant menu.
    """
    # Add "Beverages" category
    menu["Beverages"] = {"Coffee": 2.99, "Tea": 2.49}
    
    # Update price of "Steak"
    menu["Main Course"]["Steak"] = 17.99
    
    # Remove "Bruschetta" from "Starters"
    del menu["Starters"]["Bruschetta"]
    
    return menu

def main_update_menu():
    """
    Main function to update the restaurant menu.
    """
    restaurant_menu = {
        "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
        "Main Course": {"Steak": 15.99, "Salmon": 13.99},
        "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
    }
    
    updated_menu = update_menu(restaurant_menu)
    print("Updated Menu:", updated_menu)

if __name__ == '__main__':
    main_update_menu()
def open_ticket(tickets, ticket_id, customer, issue):
    """
    Open a new service ticket.
    
    Args:
        tickets (dict): The current service tickets.
        ticket_id (str): The unique ID for the new ticket.
        customer (str): The customer's name.
        issue (str): The issue description.
    
    Returns:
        dict: The updated service tickets.
    """
    # Open a new ticket with status "open"
    tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    return tickets

def update_ticket_status(tickets, ticket_id, status):
    """
    Update the status of an existing ticket.
    
    Args:
        tickets (dict): The current service tickets.
        ticket_id (str): The unique ID of the ticket to update.
        status (str): The new status ("open" or "closed").
    
    Returns:
        dict: The updated service tickets.
    """
    # Update the status of the specified ticket
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = status
    return tickets

def display_tickets(tickets, status=None):
    """
    Display all tickets or filter by status.
    
    Args:
        tickets (dict): The current service tickets.
        status (str, optional): The status to filter by ("open" or "closed").
    
    Returns:
        None
    """
    # Display tickets, optionally filtered by status
    for ticket_id, details in tickets.items():
        if status is None or details["Status"] == status:
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

def main_ticket_tracker():
    """
    Main function to track customer service tickets.
    """
    service_tickets = {
        "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
        "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    }
    
    # Open a new ticket
    service_tickets = open_ticket(service_tickets, "Ticket003", "Charlie", "Account locked")
    
    # Update the status of an existing ticket
    service_tickets = update_ticket_status(service_tickets, "Ticket001", "closed")
    
    # Display all tickets
    print("All Tickets:")
    display_tickets(service_tickets)
    
    # Display only open tickets
    print("\nOpen Tickets:")
    display_tickets(service_tickets, status="open")

if __name__ == '__main__':
    main_ticket_tracker()
