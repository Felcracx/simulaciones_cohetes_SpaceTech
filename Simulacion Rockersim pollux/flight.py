from rocketpy import Flight
from rocket import rocket
from environment import environment

"""
===============================================================================
FLIGHT.PY
-------------------------------------------------------------------------------

Aquí ocurre la simulación.

RocketPy combina:

    Environment
            +
        Rocket
            =
         Flight

Una vez creado el objeto Flight, RocketPy calcula toda la trayectoria
del cohete mediante integración numérica.

===============================================================================
"""

flight = Flight(
    rocket=rocket,
    environment=environment,
    rail_length=3,
    inclination=85,
)
print ("Simulación creada!")
print (flight.info())
rocket.draw()
flight.plots.all()