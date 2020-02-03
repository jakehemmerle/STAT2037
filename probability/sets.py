class Set:
    """
    Generic set object. events should be number of events in the set

    """

    def __init__(self, values, name='generic'):
        self.values = values


class Event(Set):
    def __init__(self, identifier, probability=None):
        super().__init__(identifier)
        self.probability = probability


class SimpleEvent(Event):
    def __init__(self, identifier, probability=None):
        super().__init__(identifier)
        self.probability = probability


class CompoundEvent(Event):
    def __init__(self, identifier, events):
        super().__init__(identifier)
        self.events = []
        for event in events:
            self.add(event)

    def add(self, event: SimpleEvent):
        self.events.append(event)
