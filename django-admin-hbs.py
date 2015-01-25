"""
Custom admin django-admin.py script

This uses custom command dispatcher that calls our makemessages
command that provides support for Handlebars makemessages
"""
from djangohbs import Admin


if __name__ == '__main__':
    utility = Admin()
    utility.execute()
