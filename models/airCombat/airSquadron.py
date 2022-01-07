from .jet import jet

class airSquadron(object):
    """docstring for airSquadron"""
    def __init__(self, arg):
        super(airSquadron, self).__init__()
        self.arg = arg
        

class airSearchSquadron(airSquadron):
    """

    docstring for airSearchSquadron

    """

    def __init__(self):
        pass

class airCoverSquadron(airSquadron):
    """

    docstring for airCoverSquadron

    """

    def __init__(self):
        pass

class airAttackSquadron(airSquadron):
    """

    docstring for airAttackSquadron

    """

    def __init__(self):
        pass


class jetSquadron(airSquadron, jet):
    """docstring for jetSquadron"""
    def __init__(self, arg):
        super(jetSquadron, self).__init__()
        self.arg = arg
        