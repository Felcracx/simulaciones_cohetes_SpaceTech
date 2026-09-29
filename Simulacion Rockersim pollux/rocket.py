from motor import motor
from rocketpy import Function, Rocket

"""
===============================================================================
ROCKET.PY
-------------------------------------------------------------------------------

Representa el cohete.
Aquí se definen únicamente las propiedades del cohete:

• Masa estructural.
• Radio.
• Momento de inercia.
• Curvas de arrastre (Drag).
• Nariz.
• Aletas.
• Paracaídas.
• Rail buttons.
• Agregar motor.

Este archivo NO simula el vuelo.

Únicamente construye el objeto Rocket.

===============================================================================
"""

power_off_drag = "POLLUX RocketSim.csv"
power_on_drag = "POLLUX RocketSim.csv"
# ==========================
# Geometría del cohete
# ==========================
BODY_LENGTH = 0.65      # Longitud del fuselaje [m]
NOSE_LENGTH = 0.15      # Longitud de la nariz [m]
BODY_RADIUS = 0.0782/2  # Radio exterior [m]
MOTOR_POSITION = 0.0    # Posición del motor respecto a la cola [m]
FIN_ROOT_CHORD = 0.09
FIN_TIP_CHORD = 0.04
FIN_SPAN = 0.065
FIN_POSITION = 0.09     # Posición de la parte superior de las aletas respecto a la cola [m]

# =============================================================================
# ESTIMACIÓN DE INERCIA (cilindro uniforme) (MEJOR SACARLO CON UN CAD)
# =============================================================================

ROCKET_MASS=1.203          # kg
ROCKET_LENGTH= BODY_LENGTH+NOSE_LENGTH

I_PITCH= (1/12)*ROCKET_MASS*(3*BODY_RADIUS**2+ROCKET_LENGTH**2)

I_ROLL= 0.5*ROCKET_MASS*BODY_RADIUS**2

INERTIA = (
    I_PITCH,
    I_PITCH,
    I_ROLL
)
rocket = Rocket(
    radius=0.0782/2,
    mass=1.203,
    inertia=INERTIA,
    center_of_mass_without_motor=0.436,
    power_off_drag=power_off_drag,
    power_on_drag=power_on_drag
)



print("Cohete creado!")
rocket.add_motor(motor, position=MOTOR_POSITION)
print("motor cargado!")
rocket.add_nose(
    length=NOSE_LENGTH,
    kind="vonKarman",
    position=BODY_LENGTH+NOSE_LENGTH
)
print("nariz cargada!")

rocket.add_trapezoidal_fins(
    n=4,
    root_chord=FIN_ROOT_CHORD,
    tip_chord=FIN_TIP_CHORD,
    span=FIN_SPAN,
    position=FIN_POSITION
)

rocket.set_rail_buttons(
    upper_button_position=0.30,
    lower_button_position=0.00,
    angular_position=120
)

import math

# ==========================
# Paracaidas principal -- con speedhole
# ==========================
CD_PARACAIDAS = 0.82   # Cd efectivo de la campana redonda con speedhole

# --- Pollux ---
DIAMETRO_PARACAIDAS_POLLUX = 1.0      # m
DIAMETRO_SPEEDHOLE_POLLUX = 0.15      # m

AREA_TOTAL_POLLUX = math.pi * (DIAMETRO_PARACAIDAS_POLLUX / 2) ** 2
AREA_SPEEDHOLE_POLLUX = math.pi * (DIAMETRO_SPEEDHOLE_POLLUX / 2) ** 2
CD_S_POLLUX = CD_PARACAIDAS * (AREA_TOTAL_POLLUX - AREA_SPEEDHOLE_POLLUX)
rocket.add_parachute(
    name="Main",
    cd_s=CD_S_POLLUX,        # m^2 -- diametro 1 m, speedhole 15 cm
    trigger="apogee",
    sampling_rate=100,
    lag=1.0
)