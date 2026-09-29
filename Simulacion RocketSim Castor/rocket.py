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

power_off_drag = "Castor_CD RocketSim.csv"
power_on_drag = "Castor_CD RocketSim.csv"
# ===================================
# Geometría del cohete (CASTOR V3)
# ===================================

# --- Ojiva (Nose Cone) ---
NOSE_LENGTH = 0.15              # Longitud de la nariz [m]
NOSE_BASE_RADIUS = 0.0782/2     # Radio en la base [m]
NOSE_KIND = "lvhaack"           # Haack series, shape parameter 0.333

# --- Cuerpo superior (diámetro grande) ---
BODY1_LENGTH = 0.25
BODY1_RADIUS = 0.0782/2

# --- Transición cónica ---
TRANSITION_LENGTH = 0.095
TRANSITION_TOP_RADIUS = 0.0782/2
TRANSITION_BOTTOM_RADIUS = 0.047/2

# --- Cuerpo inferior (diámetro pequeño, motor y aletas) ---
BODY2_LENGTH = 0.45
BODY2_RADIUS = 0.047/2

# --- Longitud total ---
ROCKET_LENGTH = NOSE_LENGTH + BODY1_LENGTH + TRANSITION_LENGTH + BODY2_LENGTH  # 0.945 m

# --- Posiciones acumuladas (0 = cola del cohete) ---
BODY2_START = 0.0
TRANSITION_START = BODY2_START + BODY2_LENGTH          # 0.45
BODY1_START = TRANSITION_START + TRANSITION_LENGTH     # 0.545
NOSE_START = BODY1_START + BODY1_LENGTH                # 0.795
NOSE_TIP = NOSE_START + NOSE_LENGTH                     # 0.945

# --- Motor y aletas ---
MOTOR_POSITION = 0.0
FIN_ROOT_CHORD = 0.08
FIN_TIP_CHORD = 0.02
FIN_SPAN = 0.05
FIN_SWEEP_LENGTH = 0.028
FIN_POSITION = 0.08

# ===================================
# ESTIMACIÓN DE INERCIA (MEJOR SACARLO CON UN CAD)
# ===================================
ROCKET_MASS = 1.536     # kg  <-- actualiza si tu masa cambió (OpenRocket dice 1536 g sin motor)

I_PITCH= (1/12)*ROCKET_MASS*(3*BODY2_RADIUS**2+ROCKET_LENGTH**2)

I_ROLL= 0.5*ROCKET_MASS*BODY2_RADIUS**2

INERTIA = (
    I_PITCH,
    I_PITCH,
    I_ROLL
)
rocket = Rocket(
    radius=BODY1_RADIUS,   # 0.047/2 — radio en la sección donde van el motor y las aletas
    mass=1.536,
    inertia=INERTIA,
    center_of_mass_without_motor=0.522,
    power_off_drag=power_off_drag,
    power_on_drag=power_on_drag
)



print("Cohete creado!")
rocket.add_motor(motor, position=MOTOR_POSITION)
print("motor cargado!")
rocket.add_nose(
    length=NOSE_LENGTH,
    kind="lvhaack",
    position=NOSE_TIP   # = 0.945 (calculado en el bloque de geometría)
)
print("nariz cargada!")
rocket.add_tail(
        top_radius=TRANSITION_TOP_RADIUS,
        bottom_radius=TRANSITION_BOTTOM_RADIUS,
        length=TRANSITION_LENGTH,
        position=BODY1_START
    )
print("transición cargada!")
rocket.add_trapezoidal_fins(
    n=4,
    root_chord=FIN_ROOT_CHORD,
    tip_chord=FIN_TIP_CHORD,
    span=FIN_SPAN,
    sweep_length=FIN_SWEEP_LENGTH,
    position=FIN_POSITION,
    radius=BODY2_RADIUS
)
rocket.set_rail_buttons(
    upper_button_position=0.765,   # cerca de la nariz
    lower_button_position=0.565,   # cerca de la cola
    angular_position=45            # coincide con OpenRocket
)
import math
DIAMETRO_PARACAIDAS_CASTOR = 1.5      # m
DIAMETRO_SPEEDHOLE_CASTOR = 0.20      # m
CD_PARACAIDAS = 0.82   # Cd efectivo de la campana redonda con speedhole
AREA_TOTAL_CASTOR = math.pi * (DIAMETRO_PARACAIDAS_CASTOR / 2) ** 2
AREA_SPEEDHOLE_CASTOR = math.pi * (DIAMETRO_SPEEDHOLE_CASTOR / 2) ** 2
CD_S_CASTOR = CD_PARACAIDAS * (AREA_TOTAL_CASTOR - AREA_SPEEDHOLE_CASTOR)
rocket.add_parachute(
    name="Main",
    cd_s=CD_S_CASTOR,        # m^2 -- diametro 1.5 m, speedhole 20 cm
    trigger="apogee",
    sampling_rate=100,
    lag=1.0
)