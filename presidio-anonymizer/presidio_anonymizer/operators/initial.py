"""Replaces the PII text entity with initials of the text."""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Replace the string with initials."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """Take the text, and return the first letter of each word found with periods between each."""
        words = text.split()
        initials = ""
        for word in words:
            initials += word[0] + ". "
        print(initials.strip())
        return initials.strip()

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize