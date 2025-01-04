# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Tenant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.Text | None
		contact_info: DF.Data | None
		email: DF.Data | None
		lease_end_date: DF.Date | None
		lease_start_date: DF.Date | None
		performance_score: DF.Int
		tenant_name: DF.Data | None
	# end: auto-generated types

	pass
