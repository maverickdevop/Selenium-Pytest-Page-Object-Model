from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_TITLE = "incorrect page title!"
    WRONG_URL = "Incorrect URL page source!"
    WRONG_TEXT = "Incorrect/Unexpected text!"
    WRONG_LIST = "Incorrect/Unexpected word in list!"
    WRONG_ELEMENT = "Element is not located on page!"
