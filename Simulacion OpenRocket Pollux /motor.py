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
    thrust_source="AeroTech_G80T.eng",
    dry_mass=0.060,
    dry_inertia=(0.001,0.001,0.0001),
    nozzle_radius=0.0145,
    grain_number=1,
    grain_density=1700,
    grain_outer_radius=0.0145,
    grain_initial_inner_radius=0.005,
    grain_initial_height=0.07,
    grain_separation=0,
    grains_center_of_mass_position=0.035,
    center_of_dry_mass_position=0.06,
    nozzle_position=0,
    burn_time=1.701
)

if __name__ == "__main__":
    motor.info()