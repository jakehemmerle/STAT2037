class Set:
    """
    Generic set object. events should be number of events in the set

    """
    def __init__(self, values, name='generic'):
        self.values = values


class Event(Set):
    def __init__(self, identifier):
        super().__init__(identifier)


class SimpleEvent(Event):
    def __init__(self, name, identifier):
        super().__init__(identifier)
        self.name = name

