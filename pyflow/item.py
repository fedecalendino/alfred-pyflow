import typing

if typing.TYPE_CHECKING:  # pragma: no cover
    from .workflow import Workflow


class Item:
    def __init__(
        self,
        title: str = "",
        subtitle: str = "",
        valid: bool = True,
        arg: str = None,
        autocomplete: str = None,
        copytext: str = None,
        largetype: str = None,
        match: str = None,
        quicklookurl: str = None,
        uid: str = None,
        type: str = "default",
    ):
        self.title: str = title
        self.subtitle: str = subtitle
        self.valid: bool = valid
        self.arg: str = arg
        self.autocomplete: str = autocomplete
        self.copytext: str = copytext
        self.largetype: str = largetype
        self.match: str = match
        self.quicklookurl: str = quicklookurl
        self.uid: str = uid
        self.type: str = type

        self.workflow: "Workflow" = None

        self._icon: dict = {}
        self._mods: dict = {}

    def set_icon_file(self, path: str):
        self._icon = {
            "path": path,
            "type": None,
        }

        return self

    def set_alt_mod(self, arg: str = None, subtitle: str = None, valid: bool = True):
        self._mods["alt"] = {
            "arg": arg,
            "subtitle": subtitle,
            "valid": valid,
        }

        return self

    def set_cmd_mod(self, arg: str = None, subtitle: str = None, valid: bool = True):
        self._mods["cmd"] = {
            "arg": arg,
            "subtitle": subtitle,
            "valid": valid,
        }

        return self

    @property
    def serialized(self) -> dict:
        return {
            "arg": self.arg,
            "autocomplete": self.autocomplete,
            "icon": self._icon,
            "match": self.match,
            "mods": self._mods,
            "quicklookurl": self.quicklookurl,
            "subtitle": self.subtitle,
            "text": {
                "copy": self.copytext,
                "largetype": self.largetype,
            },
            "title": self.title,
            "uid": self.uid,
            "type": self.type,
            "valid": self.valid,
        }
