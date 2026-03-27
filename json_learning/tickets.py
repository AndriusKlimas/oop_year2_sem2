class Ticket:
    def __init__(self, ticket_id: int, title: str, desc: str, status: str, assigned_to: str):
        self.ticket_id = ticket_id
        self.title = title
        self.description = desc
        self.status = status
        self.assigned_to = assigned_to

    def __str__(self) -> str:
        return f"Ticket {self.ticket_id}: {self.title}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{{ticket_id={self.ticket_id}, title={self.title}, description={self.description}, status={self.status}, assigned_to={self.assigned_to}}}"


    @classmethod
    def from_dict(cls, ticket_dict_obj):
        try:
            ticket_id = ticket_dict_obj["ticket_id"]
            title = ticket_dict_obj["title"]
            description = ticket_dict_obj["description"]
            status = ticket_dict_obj["status"]
            assigned_to = ticket_dict_obj["assigned_to"]
            return cls(ticket_id, title, description, status, assigned_to)
        except KeyError as e:
            print(f"Error occured {e} in {ticket_dict_obj}")
            raise KeyError(f"json decerilisation error:{e}")
