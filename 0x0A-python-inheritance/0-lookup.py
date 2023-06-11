"""Description: A function that looks for a list of
available attributes and methods of an objects"""


def lookup(obj):
    """Looks into an objects and returns a
    list of method and attributes"""
    return(dir(obj))
