__author__ = 'nampnq'

import os

CONFIG = {
        'debug': True,
        'webapp2_extras.jinja2': {
            'template_path': os.path.join(os.getcwd(),"templates"),
            'globals': {
                'title': 'GDayX Vietnam',
                "gpluspage":"//plus.google.com/109409100303847423101",
                "fbgdg":"https://www.facebook.com/gdgviet",
                "fbgbg":"https://www.facebook.com/groups/gbgvietnam/",
                "gplusgdg":"https://plus.google.com/106004400398954649440/posts",
                "gplusgbg":"https://plus.google.com/114280998103503452953/posts",
            },
        },
}