import os
import template_ui
import template2_ui

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
GLOBAL_DIR = os.path.dirname(os.path.abspath(__file__))

PAGES = {
    "template" : os.path.join(GLOBAL_DIR, "template.ui"),
    "template_2" : os.path.join(GLOBAL_DIR, "template2.ui"),
}

PAGES_UI = {
    "template" : template_ui.Ui_Termplate(),
    "template_2" : template2_ui.Ui_Template(),
}

PAGES_INDEX = {
    "template" : 0,
    "template_2" : 1
}

PAGES_TITLES = {
    "template" : 'Template',
    "template_2" : 'Template 2'
}