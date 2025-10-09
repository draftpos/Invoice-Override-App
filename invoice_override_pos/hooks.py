app_name = "invoice_override_pos"
app_title = "Invoice Override POS"
app_publisher = "havano pos"
app_description = "Custom hooks to export Sales Invoice as TXT"
app_email = "chirovemunyaradzi@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "invoice_override_pos",
# 		"logo": "/assets/invoice_override_pos/logo.png",
# 		"title": "Invoice Override POS",
# 		"route": "/invoice_override_pos",
# 		"has_permission": "invoice_override_pos.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/invoice_override_pos/css/invoice_override_pos.css"
# app_include_js = "/assets/invoice_override_pos/js/invoice_override_pos.js"

# include js, css files in header of web template
# web_include_css = "/assets/invoice_override_pos/css/invoice_override_pos.css"
# web_include_js = "/assets/invoice_override_pos/js/invoice_override_pos.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "invoice_override_pos/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "invoice_override_pos/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "invoice_override_pos.utils.jinja_methods",
# 	"filters": "invoice_override_pos.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "invoice_override_pos.install.before_install"
# after_install = "invoice_override_pos.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "invoice_override_pos.uninstall.before_uninstall"
# after_uninstall = "invoice_override_pos.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "invoice_override_pos.utils.before_app_install"
# after_app_install = "invoice_override_pos.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "invoice_override_pos.utils.before_app_uninstall"
# after_app_uninstall = "invoice_override_pos.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "invoice_override_pos.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# doc_events = {
#     "Sales Invoice": {
#         "after_insert": "invoice_override_pos.invoice_override_pos.sales_invoice_hooks.save_invoice_txt_hook"
#     }
# }
# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"invoice_override_pos.tasks.all"
# 	],
# 	"daily": [
# 		"invoice_override_pos.tasks.daily"
# 	],
# 	"hourly": [
# 		"invoice_override_pos.tasks.hourly"
# 	],
# 	"weekly": [
# 		"invoice_override_pos.tasks.weekly"
# 	],
# 	"monthly": [
# 		"invoice_override_pos.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "invoice_override_pos.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "invoice_override_pos.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "invoice_override_pos.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["invoice_override_pos.utils.before_request"]
# after_request = ["invoice_override_pos.utils.after_request"]

# Job Events
# ----------
# before_job = ["invoice_override_pos.utils.before_job"]
# after_job = ["invoice_override_pos.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"invoice_override_pos.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

