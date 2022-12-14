import json
import logging
from calendar import c

import azure.functions as func

from shared.days_until import get_days_until


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Calculate days until next thu"""

    msg, color = get_days_until(5, time=(15, 0, 0))
    # return shield.io json
    return func.HttpResponse(
        json.dumps(
            {
                "schemaVersion": 1,
                "label": "Next Recording in",
                "message": msg,
                "color": color,
            }
        )
    )
