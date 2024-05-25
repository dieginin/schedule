class Member:
    def __init__(
        self,
        id: int,
        name: str,
        initials: str,
        color: str,
    ):
        self._id = id
        self.name = name
        self.initials = initials
        self.color = color

    @property
    def id(self) -> int:
        return self._id
