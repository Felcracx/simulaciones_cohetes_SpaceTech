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
    grain_density=1800,                  # estimado, sin dato oficial de densidad
    grain_outer_radius=0.0145,           # estimado (radio interno de la carcasa de 29mm)
    grain_initial_inner_radius=0.005,    # estimado
    grain_initial_height=0.20,           # estimado (a partir de masa de propelente/densidad)
    grains_center_of_mass_position=0.10, # estimado
    center_of_dry_mass_position=0.11,    # estimado
    nozzle_position=0,
    burn_time=2.072                        # s — dato certificado (verificar valor exacto en el .eng)
)

if __name__ == "__main__":
    motor.info()