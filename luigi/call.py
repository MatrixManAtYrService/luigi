import luigi.define as defined

class InterfaceError(Exception):
    pass

def fromcli(func, **kwargs):
    pass

def to(func, val):
    pass

def path(val, start=None, end=None):
    missing = []
    if not start:
        missing.append('start')
    if not end:
        missing.append('end')
    if any(missing):
        raise InterfaceError("required kwarg missing: " + ','.join(missing))

    path(val, start, end)

def path(val, start, end):
    pass

def path(val, hops):
    pass
