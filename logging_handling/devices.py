from __future__ import annotations

class Device:
    def __init__(self, name:str, interface_type:str):
        #checking if anything in it
        if name:
            self._name = name

        if interface_type:
            self._interface_type = interface_type

        self.__component = []

    def add_component(self, component: Component) -> None:
        if component.get_interface() != self._interface_type:
            raise ValueError(f"Component {component.get_name()} employs incorrect interface")

        self.__component.append(component)

    def get_component(self) -> list[Component]:
        return list(self.__component)


class Component:
    def __init__(self, name:str, type:str, interface:str, job:str):
        if name:
            self._name = name

        if type:
            self._type = type

        if interface:
            self._interface = interface

        if job:
            self._job = job

    def get_interface(self) -> str:
        return str(self._interface)

    def get_name(self) -> str:
        return self._name
