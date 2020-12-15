from frappe import _


def get_data():
    return [
        {
            "module_name": "jobPRO",
            "color": "grey",
            "icon": "fa fa-star",
                    "type": "module",
                    "label": _("jobPRO"),
                    "items": [
                        {
                            "type": "doctype",
                            "name": "Sign Up",
                            "icon": "fa fa-star",
                            "label": _("Sign Up"),
                            "description": _("jobPRO Sign Up"),
                        },
                        {
                            "type": "doctype",
                            "name": "Job Post",
                            "icon": "fa fa-star",
                            "label": _("Job Post"),
                            "description": _("jobPRO job posting"),
                        },
                        {
                            "type": "doctype",
                            "name": "Candidate",
                            "icon": "fa fa-star",
                            "label": _("Candidate"),
                            "description": _("jobPRO Candidate "),
                        }
                    ]
        }
    ]
