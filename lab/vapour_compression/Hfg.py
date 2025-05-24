from CoolProp.CoolProp import PropsSI

# Define fluid
fluid = 'R134a'

# Input: Saturation pressure in bar
pressure_bar = 8.880324  # You can change this value
pressure_Pa = pressure_bar * 100000  # Convert bar to Pa

# Get saturation temperature (in K → °C)
T_sat_K = PropsSI('T', 'P', pressure_Pa, 'Q', 0, fluid)
T_sat_C = T_sat_K - 273.15

# Get enthalpies
hf = PropsSI('H', 'P', pressure_Pa, 'Q', 0, fluid) / 1000  # kJ/kg
hg = PropsSI('H', 'P', pressure_Pa, 'Q', 1, fluid) / 1000  # kJ/kg
hfg = hg - hf  # Latent heat

# Output
print(f"At {pressure_bar:.2f} bar:")
print(f"  Saturation Temperature: {T_sat_C:.2f} °C")
print(f"  hf (saturated liquid):  {hf:.2f} kJ/kg")
print(f"  hg (saturated vapor):   {hg:.2f} kJ/kg")
print(f"  hfg (latent heat):      {hfg:.2f} kJ/kg")
