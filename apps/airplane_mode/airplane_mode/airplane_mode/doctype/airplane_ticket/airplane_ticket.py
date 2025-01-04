import frappe
import random
from frappe.model.document import Document
from frappe import _

class AirplaneTicket(Document):
    def validate(self):
        if not self.flight_price:
            frappe.throw("Please provide a price")
        
        total_amount = 0
        for item in self.items:
            total_amount += item.amount

        self.total_amount = total_amount + self.flight_price

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("The ticket can only be submitted if the status is 'Boarded'.")

    def before_insert(self):
        self.check_flight_capacity()
        
        if not self.seat:
            random_number = random.randint(1, 99)
            random_letter = random.choice('ABCDE')
            self.seat = f"{random_number} {random_letter}"

    def check_flight_capacity(self):
        flight = frappe.get_doc("Airplane Flight", self.flight)
        airplane = frappe.get_doc("Airplane", flight.airplane)
        capacity = airplane.capacity
        
        existing_tickets = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})

        if existing_tickets >= capacity:
            frappe.throw(_("Cannot create a new ticket. The flight has reached its full capacity of {0} seats.").format(capacity))

def validate_ticket_creation(doc, method):
    flight = frappe.get_doc("Airplane Flight", doc.flight)
    airplane = frappe.get_doc("Airplane", flight.airplane)
    capacity = airplane.capacity
    
    existing_tickets = frappe.db.count("Airplane Ticket", filters={"flight": doc.flight})

    if existing_tickets >= capacity:
        frappe.throw(_("Cannot create a new ticket. The flight has reached its full capacity of {0} seats.").format(capacity))

@frappe.whitelist()
def update_gate_number(flight_id, new_gate_number):
    tickets = frappe.get_all('Airplane Ticket', filters={'flight': flight_id}, fields=['name'])
    
    for ticket in tickets:
        frappe.db.set_value('Airplane Ticket', ticket.name, 'gate_number', new_gate_number)

    frappe.db.commit()

    frappe.log("Updated gate number for tickets of flight: {0} to {1}".format(flight_id, new_gate_number))
