# Copyright (c) 2024, Maxim S and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class dcDocTypeFilters(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		condition: DF.Data | None
		field: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		value: DF.Data | None
	# end: auto-generated types

	pass
