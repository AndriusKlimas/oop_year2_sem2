import logging
from tickets import Ticket, FeatureRequest, TicketException

logger = logging.getLogger(__name__)

class TicketDataAccess:

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
