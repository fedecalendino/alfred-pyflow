import os
from enum import Enum

ROOT = "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources"


class Icon(str, Enum):
    ALERT_STOP = os.path.join(ROOT, "AlertStopIcon.icns")
