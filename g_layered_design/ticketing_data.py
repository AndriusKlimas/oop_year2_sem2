import os
import logging
from tickets import Ticket, FeatureRequest, TicketException

logger = logging.getLogger(__name__)

class TicketDataAccess:

    def __init__(self,filename):
        if not filename:
            raise ValueError('filename cannot be None')

        if not os.path.exists(filename):
            raise FileNotFoundError("No such file: '%s'" % filename)

        self._filename = filename

    def read_file(self, filename: str) -> tuple[list[Ticket], dict[str, list[Ticket]]]:
        unassigned_tickets = []
        assigned_tickets = {}

        with open(filename) as file:
            for line in file:
                ticket = self.parse_ticket(line)
                if ticket is None:
                    continue

                agent = ticket.get_assigned_agent()

                if agent == "":
                    unassigned_tickets.append(ticket)
                    logger.info(f"Unassigned ticket retrieved: {ticket}")
                else:
                    agent_list = assigned_tickets.setdefault(agent.lower(), [])
                    agent_list.append(ticket)
                    logger.info(f"Assigned ticket retrieved for {agent}: {ticket}")

        return unassigned_tickets, assigned_tickets

    def parse_ticket(self, text: str) -> Ticket | None:
        parts = text.strip().split("%%")

        try:
            ticket_type = parts[0]
            ticket_id = int(parts[1])
            title = parts[2]
            desc = parts[3]
            status = parts[4]
            assigned_to = parts[5]

            if ticket_type.lower() == "ticket":
                return self.build_ticket(ticket_id, title, desc, status, assigned_to)
            else:
                requested = parts[6]
                approval = parts[7]
                return self.build_feature_request(ticket_id, title, desc, status, assigned_to, requested, approval,
                                                  text)

        except Exception as e:
            logger.warning(f"line is skipped: {text}")
            return None

    def build_ticket(self, ticket_id, title, desc, status, assigned_to):
        ticket = Ticket(ticket_id, title, desc)
        ticket.update_status(status)
        if assigned_to != " ":
            ticket.assign_to(assigned_to)
        return ticket

    def build_feature_request(self, ticket_id, title, desc, status, assigned_to, requested, approval, line):
        ticket = FeatureRequest(ticket_id, title, desc, requested)
        ticket.update_status(status)
        if assigned_to != "":
            ticket.assign_to(assigned_to)

        match approval.upper():
            case "APPROVED":
                ticket.approve()
            case "REJECTED":
                ticket.reject()
            case "PENDING":
                pass
            case _:
                raise TicketException(f"Illegal approval status ({approval}) in line: {line}")

        return ticket
