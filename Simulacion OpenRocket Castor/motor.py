from rocketpy import SolidMotor

"""
===============================================================================
MOTOR.PY
-------------------------------------------------------------------------------

Representa el sistema de propulsión del cohete.

Aquí se define completamente el motor:

• Curva de empuje.
• Tiempo de combustión.
• Masa del propelente.
• Geometría del grano.
• Tobera.
• Centro de masa.

===============================================================================
"""

motor = SolidMotor(
    thrust_source="HP-H135W.eng",       # archivo RASP descargado de ThrustCurve
    dry_mass=0.130,                      # kg — 212g totales - 82g propelente (dato certificado)
    dry_inertia=(0.001, 0.001, 0.0001),  # estimado, sin dato oficial de AeroTech
    nozzle_radius=0.0145,                # m — 29mm de diámetro / 2 (dato certificado)
    grain_number=1,
    grain_separation=0,          # m -- no aplica, solo hay 1 grano
    grain_density=1800,                  # estimado
    grain_outer_radius=0.0125,           # estimado, considerando pared de la carcasa
    grain_initial_inner_radius=0.006,    # estimado
    grain_initial_height=0.122,          # ajustado para dar ~82 g de propelente (dato certificado)
    grains_center_of_mass_position=0.075,# estimado
    center_of_dry_mass_position=0.108,   # estimado (mitad de los 216mm de longitud total)
    nozzle_position=0,
    burn_time=2.072                        # s — dato certificado (verificar valor exacto en el .eng)
)

if __name__ == "__main__":
    motor.info()