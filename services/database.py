from tinydb import Query, TinyDB

from models import Member


class Database:
    def __init__(self):
        db = TinyDB("database.json")
        self._members = db.table("members")

    @property
    def members(self) -> list[Member]:
        return [
            Member(member["id"], member["name"], member["initials"], member["color"])
            for member in self._members.all()
            if member
        ]

    def _check_existence(self, table, **kwargs) -> str | None:
        for key, value in kwargs.items():
            if table.search(Query()[key] == value):
                return f"Existing {key}"
        return

    def insert_member(self, name: str, initials: str, color: str) -> str:
        if exists := self._check_existence(
            self._members, name=name, initials=initials, color=color
        ):
            return exists

        id = self._members.insert(
            {
                "id": 0,
                "name": name,
                "initials": initials,
                "color": color,
            }
        )
        self._members.update({"id": id}, doc_ids=[id])

        return f"[{initials}] {name} inserted"
