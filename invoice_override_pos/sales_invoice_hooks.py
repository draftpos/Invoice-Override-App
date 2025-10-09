import frappe
import os
import json

# ----------------------------
# 1️⃣ Hook function for after_insert
# ----------------------------
def save_invoice_txt_hook(doc, method=None):
    """
    Hook: Automatically save Sales Invoice as TXT after insert
    """
    save_invoice_txt_to_windows(doc)


# ----------------------------
# 2️⃣ Whitelisted function for client download
# ----------------------------
@frappe.whitelist()
def download_invoice_json(invoice_name):
    """
    Returns Sales Invoice data as dict for browser download
    """
    doc = frappe.get_doc("Sales Invoice", invoice_name)
    return doc.as_dict()


# ----------------------------
# 3️⃣ Shared helper function
# ----------------------------
def save_invoice_txt_to_windows(doc):
    """
    Writes Sales Invoice doc to C:\Invoice Folder as TXT (JSON-structured)
    """
    try:
        data = doc.as_dict()

        # Windows folder path
        text_dir = r"C:\Invoice Folder"
        os.makedirs(text_dir, exist_ok=True)

        # File name and full path
        file_name = f"{doc.name}.txt"
        file_path = os.path.join(text_dir, file_name)

        # Write JSON-structured TXT
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, default=str)

        # Notify user
        print(f"✅ TXT file saved for {doc.name} at {file_path}")
        frappe.msgprint(f"✅ TXT file saved at {file_path}")

    except Exception as e:
        print(f"{str(e)}, Sales Invoice TXT Export Error")
        frappe.log_error(message=str(e), title="Sales Invoice TXT Export Error")
        frappe.msgprint(f"❌ Error saving TXT: {str(e)}")
