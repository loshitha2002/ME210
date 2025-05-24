from CoolProp.CoolProp import PropsSI

# Define fluid and state conditions
fluid = 'R134a'
temperature_C = 80        # Temperature in Celsius
pressure_bar = 8.80324            # Pressure in bar

# Convert to required SI units
temperature_K = temperature_C + 273.15
pressure_Pa = pressure_bar * 100000  # bar to Pa

# Get specific enthalpy in J/kg
enthalpy = PropsSI('H', 'T', temperature_K, 'P', pressure_Pa, fluid)
enthalpy_kJkg = enthalpy / 1000  # Convert to kJ/kg

# Optional: Check phase to ensure it's superheated
phase = PropsSI('PHASE', 'T', temperature_K, 'P', pressure_Pa, fluid)

# Display results
print(f"At {temperature_C}°C and {pressure_bar} bar:")
print(f"Phase: {phase}")
print(f"Specific enthalpy of R-134a is {enthalpy_kJkg:.2f} kJ/kg")
