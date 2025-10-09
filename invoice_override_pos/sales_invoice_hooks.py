
import frappe
import os
import json

import frappe
import os
import json

def after_save(doc, method=None):
    """
    Export Sales Invoice as TXT (JSON structured) to Windows folder C:\Invoice Folder
    and create/update ERPNext File record.
    """
    print("---------------new override-------------------------")
    try:
        # Convert the doc to dictionary
        data = doc.as_dict()

        # Windows folder path
        text_dir = r"C:\Invoice Folder"  # raw string for folder with space
        os.makedirs(text_dir, exist_ok=True)

        # File name and path
        file_name = f"{doc.name}.txt"
        file_path = os.path.join(text_dir, file_name)

        # Write JSON-structured TXT
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, default=str)

        # --- ERPNext File record ---
        # Delete existing File record if exists
        existing_file = frappe.db.exists("File", {"file_name": file_name})
        if existing_file:
            frappe.delete_doc("File", existing_file)

        # Insert new File record pointing to Windows path
        file_doc = frappe.get_doc({
            "doctype": "File",
            "file_name": file_name,
            "attached_to_doctype": "Sales Invoice",
            "attached_to_name": doc.name,
            "is_private": 1,
            "file_url": f"file://{file_path}"  # absolute path
        })
        file_doc.insert(ignore_permissions=True)
        frappe.db.commit()

        print(f"✅ TXT file saved for {doc.name} at {file_path}")
        frappe.msgprint("Saved in path")

    except Exception as e:
        print(f"{str(e)}, Sales Invoice TXT Export Error")
        frappe.throw(f"{str(e)}, Sales Invoice TXT Export Error")
