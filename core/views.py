from django.db import connections
from django.db.utils import OperationalError

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def health_check(request):
    db_ok = True
    try:
        db_conn = connections["default"]
        db_conn.cursor()
    except OperationalError:
        db_ok = False

    data = {
        "status": "ok",
        "database": "ok" if db_ok else "error",
    }

    return Response(
        data,
        status=status.HTTP_200_OK if db_ok else status.HTTP_503_SERVICE_UNAVAILABLE,
    )
