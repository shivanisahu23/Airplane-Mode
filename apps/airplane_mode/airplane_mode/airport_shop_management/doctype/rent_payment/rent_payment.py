# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RentPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		payment_amount: DF.Currency
		payment_date: DF.Date | None
		receipt: DF.Data | None
		shop: DF.Link | None
		tenant: DF.Link | None
	# end: auto-generated types

	pass
