from devices import Device
from devices import Component

def create_component() -> Component:
    name = input("Enter the name: ")
    #This one will fuck an error at you if not the same
    ctype = input("Enter the type: ")
    #This one can be anyhtign you want
    interface = input("Enter the interface: ")
    job = input("Enter the job: ")

    component = Component(name, ctype, interface, job)
    return component

if __name__ == "__main__":

    my_machine = Device("my laptop", "USB-C")
    components = []


    for i in range(2):
        component = create_component()
        components.append(component)

    for component in components:
        try:
            my_machine.add_component(component)

        except ValueError as e:
            print(f"Exception occured: {e.args[0]}")
            print(f"Not able to add {component.get_name()} as incorrect type")
