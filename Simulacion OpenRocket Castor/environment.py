from rocketpy import Environment
"""
===============================================================================
ENVIRONMENT.PY
-------------------------------------------------------------------------------

Representa el entorno donde se realizará el lanzamiento.

Este objeto contiene toda la información del ambiente, por ejemplo:

• Latitud y longitud del sitio de lanzamiento.
• Elevación sobre el nivel del mar.
• Condiciones atmosféricas.
• Viento.
• Temperatura.
• Presión.

Todo aquello que NO pertenece al cohete vive aquí.

===============================================================================
"""
# =============================================================================
# UBICACIÓN
# =============================================================================

LATITUDE = 6.2442
LONGITUDE = -75.5812
ELEVATION = 1495      # ajusta segun tu sitio exacto de lanzamiento en Medellin

# =============================================================================
# FECHA
# =============================================================================

YEAR = 2026
MONTH = 7
DAY = 7
HOUR = 12

# =============================================================================
# VIENTO
# =============================================================================

WIND_U = 3.0      # viento al este positivo m/s 
WIND_V = 3.0      # viento al norte positivo m/s

environment = Environment(
    latitude=LATITUDE,
    longitude=LONGITUDE,
    elevation=ELEVATION
)

environment.set_date((YEAR, MONTH, DAY, HOUR))

environment.set_atmospheric_model(
    type="custom_atmosphere",
    wind_u=WIND_U,
    wind_v=WIND_V,
)