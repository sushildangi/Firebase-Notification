class MyType(type):
    def __new__(cls, name, bases, attrs):
        if name.startswith('None'):
            return None
        newattrs = {}
        for attrname, attrvalue in attrs.iteritems():
            if getattr(attrvalue, 'is_hook', 0):
