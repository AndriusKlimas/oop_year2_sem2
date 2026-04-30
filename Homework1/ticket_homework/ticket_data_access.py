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
