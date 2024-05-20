# Copyright (c) 2024, Maxim S and contributors
# For license information, please see license.txt

# import frappe
import json
import frappe
from frappe.model.document import Document


class dcDocType(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from desk_configurator.desk_configurator.doctype.dcdoctype_addfields.dcdoctype_addfields import dcDocTypeAddFields
		from desk_configurator.desk_configurator.doctype.dcdoctype_filters.dcdoctype_filters import dcDocTypeFilters
		from frappe.types import DF

		add_fields: DF.Table[dcDocTypeAddFields]
		code_hpie: DF.Code | None
		doctype_config: DF.Link
		doctype_path: DF.Data | None
		filters: DF.Table[dcDocTypeFilters]
		get_indicator: DF.Code | None
		has_indicator_for_draft: DF.Check
		hide_name_column: DF.Check
		hide_name_filter: DF.Check
		list_view_js_path: DF.Data | None
	# end: auto-generated types

	
	@property
	def doctype_path(self):
		return get_doctype_folder_path(self.doctype_config)
	@property
	def list_view_js_path(self):
		return get_doctype_config_js(self.doctype_config, False)
	@property
	def code_hpie(self):
		context = {
			'doctype_config': self.doctype_config,
			'hide_name_column': self.hide_name_column,
			'hide_name_filter': self.hide_name_filter,
			'has_indicator_for_draft': self.has_indicator_for_draft,
			'add_fields': self.add_fields,
			'filters': self.filters,
			'get_indicator': self.get_indicator,
		}
		return render_my_template(context, False)

def get_doctype_config_js(doctype:str, is_calendar:bool = False):
	config_js = 'calendar' if is_calendar else 'list'	
	doctype_folder_path = get_doctype_folder_path(doctype)
	doctype_list_view_js =  frappe.utils.os.path.join(doctype_folder_path, doctype.lower().replace(' ', '_')+f'_{config_js}.js')
	return doctype_list_view_js

def get_doctype_folder_path(doctype):
		module = frappe.get_meta(doctype).module  # Get the module name from the doctype
		module_path = frappe.get_module_path(module)  # Get the module path
		doctype_folder_path = frappe.utils.os.path.join(module_path, 'doctype', doctype.lower().replace(' ', '_'))  # Construct the doctype folder path
		return doctype_folder_path

def render_my_template(context, is_calendar:bool = False):
	config_js = 'calendar' if is_calendar else 'list'	
	# Define the path to your template
	template_path = f'desk_configurator/templates/doctype_{config_js}.jinja'
	
	# Load the template
	template = frappe.get_template(template_path)
	
	# Render the template with context data
	rendered_html = template.render(context)
	
	return rendered_html