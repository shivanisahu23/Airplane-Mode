# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Shop(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport_address: DF.Link | None
		area: DF.Float
		contract_expiry_date: DF.Date | None
		contract_start_date: DF.Date | None
		is_published: DF.Check
		rent_amount: DF.Currency
		route: DF.Data | None
		shop_name: DF.Data | None
		shop_number: DF.Data | None
		status: DF.Literal["Available", "Occupied"]
		tenant: DF.Link | None
	# end: auto-generated types

	pass
