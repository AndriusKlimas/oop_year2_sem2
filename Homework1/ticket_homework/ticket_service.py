from tickets import Ticket
from ticketing_system import *
class TicketService:
    def __init__(self, assigned: dict[str, list[Ticket]] = None, unassigned: list[str] = None):
        self.__assigned_tickets = dict.copy(assigned) if assigned else {}
        self.__unassigned_tickets = list.copy(unassigned) if unassigned else []

    def get_tickets_for_agent(self, agent: str):
        if agent.lower() not in self.__assigned_tickets:
            return None

        return  self.__assigned_tickets[agent.lower()]


    def get_agents(self):
        return list(self.__assigned_tickets.keys())


    def get_ticket_list(self):
        if len(self.__assigned_tickets) == 0:
            return None
        return list(self.__assigned_tickets.values())


    def assign_next_ticket_1(self, agent: str):
        #this will need to check the unassigned dict and then give it to an agent and move it to the assigned queue
        #agent will be passed by the ui
        #need to get the first itema in the list and assignt the agent to it
        #then remove from unassigned list and then add it to teh assigned dict
        if len(self.__unassigned_tickets) == 0:
            return None

        new_ticket = self.__unassigned_tickets[0]
        agent = ""
        try:
            agent = input("Please enter agent name to be assigned a ticket: ")
            # Link to specified agent
            new_ticket.assign_to(agent)

            ticketing_system.assign_ticket(agent, self.__assigned_tickets ,new_ticket)

            self.__unassigned_tickets.pop(0)

        except Exception as e:
            return "message"










        print("Under development")

