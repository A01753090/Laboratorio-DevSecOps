"""Servicio educativo de telemetría: no se conecta a sistemas OT reales."""

ALLOWED_OPERATION = "read"


ALLOWED_OPERATIONS = frozenset({"read"})


def is_operation_allowed(operation: str) -> bool:
    """Lista blanca con denegación por defecto: solo 'read'."""
    return operation in ALLOWED_OPERATIONS


def get_telemetry(operation: str, measurement: str = "temperature") -> dict:
    """Devuelve datos simulados si la operación está autorizada."""
    if not is_operation_allowed(operation):
        return {"status": "denied", "operation": operation}

    readings = {"temperature": 24.5, "pressure": 1.2}
    if measurement not in readings:
        return {"status": "not_found", "measurement": measurement}
    return {"status": "ok", "measurement": measurement, "value": readings[measurement]}
