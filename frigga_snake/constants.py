import re

NAME_CHARS = "a-zA-Z0-9._"
NAME_HYPHEN_CHARS = "-a-zA-Z0-9._"
PUSH_FORMAT = "v([0-9]{3})"
LABELED_VAR_SEPARATOR = "0"
LABELED_VARIABLE = "[a-zA-Z][" + LABELED_VAR_SEPARATOR + "][a-zA-Z0-9]+"

COUNTRIES_KEY = "c"
DEV_PHASE_KEY = "d"
HARDWARE_KEY = "h"
PARTNERS_KEY = "p"
REVISION_KEY = "r"
USED_BY_KEY = "u"
RED_BLACK_SWAP_KEY = "w"
ZONE_KEY = "z"

NAME_PATTERN = re.compile("^([" + NAME_CHARS + "]+)(?:-([" + NAME_CHARS + "]*))?(?:-([" + NAME_HYPHEN_CHARS + "]*?))?$")
PUSH_PATTERN = re.compile("^([" + NAME_HYPHEN_CHARS + "]*)-(" + PUSH_FORMAT + ")$")
LABELED_VARS_PATTERN = re.compile("^([" + NAME_HYPHEN_CHARS + "]*?)((-" + LABELED_VARIABLE + ")*)$")

APP_VERSION_PATTERN = re.compile("([" + NAME_HYPHEN_CHARS + "]+)-([0-9.a-zA-Z]+)-(\\w+)(?:[.](\\w+))?(?:\\/([" + NAME_HYPHEN_CHARS + "]+)\\/([0-9]+))?")