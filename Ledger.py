
class Ledger(object) :
    def __init__(self) :
        self._list = []
        pass

    def add_transaction(self, transaction) :
        self._list.append(transaction)
        pass

    def __delitem__(self, key) :
        self._list.__delitem__(key)

    def __getitem__(self, key) :
        return self._list.__getitem__(key)

    def __setitem__(self, key) :
        self._list.__setitem__(key)

    def __contains__(self, key) :
        for k in self._list :
            if k is key : return True
        return False

    def __len__(self) :
        return len(self._list)

    def keys(self) :
        list_of_lists = [list(t.keys()) for t in self]
        _list = [item for sublist in list_of_lists for item in sublist]
        return set(_list)
