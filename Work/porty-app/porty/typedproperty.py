"""
Typed property definition.

Descriptors allowing to control data type of attributes.

© Denis Shelemekh, 2020
"""

from typing import Any


def typedproperty(name: str, expected_type: Any) -> Any:
    """
    Creates property setter and getter allowing for data type control.

    Args:
        name: String - name of the property.
        expected_type: Any - expected type of the property.
    Raises:
        TypeError: When value supplied to setter doesn't match expected type.
    """

    private_name = '_' + name

    @property
    def prop(self) -> Any:
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value: Any) -> None:
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected {expected_type}")
        setattr(self, private_name, value)

    return prop


# Shortcuts
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
