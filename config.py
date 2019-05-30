import os
from collections import namedtuple

# EDIT
USERNAME = '...'
PASSWORD = '...'

Path = namedtuple("Path", ["courses", "name"])

PATHS = [
    Path(name = None, courses = [
        'user-experience-for-web-designers'
    ]),
    Path(name = "UX Foundations", courses = [
        'ux-foundations-prototyping-2',
        'ux-foundations-interaction-design',
        'ux-foundations-research',
        'ux-foundations-information-architecture',
        'ux-foundations-style-guides-and-design-systems',
        'ux-foundations-logic-and-content',
        'ux-foundations-content-strategy',
        'ux-foundations-accessibility',
        'ux-foundations-multidevice-design-2',
        'ux-foundations-making-the-case-for-usability-testing',
        'ux-foundations-usability-testing'
    ])
]

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), "downloads")
USE_PROXY = False
MULTI_THREAD = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None
