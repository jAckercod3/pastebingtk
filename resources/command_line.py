# -*- coding: utf-8 -*-


# This file defines the functions for working with command line arguments.


# Import the pastebin API wrapper.
from resources.pastebin_python.pastebin import PastebinPython
# Import the API exceptions.
from resources.pastebin_python.pastebin_exceptions import PastebinBadRequestException, PastebinFileException, PastebinHTTPErrorException, PastebinNoPastesException
# Import the API options.
from resources.pastebin_python.pastebin_options import OPTION_DELETE, OPTION_LIST, OPTION_PASTE, OPTION_TRENDS, OPTION_USER_DETAILS


def upload(args, dev_key):
    """Uploads text to pastebin.com."""
    
    # Initalize the PastebinPython object.
    api = PastebinPython(api_dev_key = dev_key)
    
    # Get the text.
    if args[1] == "uploadfile":
        text = open(args[2], "r").read()
    else:
        text = args[2]
    
    # Get the other fields.
    title = ""
    format_ = ""
    exposure = 0
    exposure_str = "public"
    expiration = ""
    if len(args) > 3:
        title = args[3]
    if len(args) > 4:
        format_ = args[4]
    if len(args) > 5:
        exposure_str = args[5]
    if len(args) > 6:
        expiration = args[6]
    
    # Change fields as needed.
    if exposure_str == "unlisted":
        exposure = 1
    elif exposure_str == "private":
        exposure = 2
    
    # Send the paste.
    url = api.createPaste(api_paste_code = text, api_paste_name = title, api_paste_format = format_, api_paste_private = exposure,
                               api_paste_expire_date = expiration)
    
    # Return the paste URL.
    return url


def download(args, dev_key):
    """Downloads text from pastebin.com."""
    
    # Initalize the PastebinPython object.
    api = PastebinPython(api_dev_key = dev_key)
    
    # Get the paste.
    paste = api.getPasteRawOutput(api_paste_key = args[2])
    
    # Return the paste text.
    return paste