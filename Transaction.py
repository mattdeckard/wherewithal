from magicdate import magicdate

class Transaction(object) :
    def __init__(self) :
        self._dict = {}
        self['Date'] = 'today'

    def __getitem__(self, key) :
        return self._dict.__getitem__(key)

    def __setitem__(self, key, value) :
        new_value = value
        if key == 'Date' :
            new_value = magicdate(value)
        self._dict.__setitem__(key, new_value)

    def __contains__(self, key) :
        return self._dict.__contains__(key)

    def sort_key(self) :
        return self['Date']

    def keys(self) :
        return self._dict.keys()
