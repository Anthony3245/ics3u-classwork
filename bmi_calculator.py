# Height in m: 1.75
# Weight in kg: 73
# The BMI is 23.83673
height_m= 1.75
weight_kg= 73
BMI_calculator = weight_kg/height_m ** 2
print(f"your BMI is {round(BMI_calculator,2)} ")

# Height in inches: 69
# Weight in pounds: 160
# The BMI is 23.625289
height_inches = 69
weight_pounds = 160 
height_m = height_inches * 0.0254
weight_kg = weight_pounds * 0.453592
BMI_calculator = weight_kg/height_m ** 2
print(f"your BMI is {round(BMI_calculator,2)} ")

# Height (feet only): 5
# Height (inches): 9
# Weight in pounds: 160
# The BMI is 23.625289

height_feet = 5
height_inches = 5
total_height_inches = height_feet*12 + height_inches
weight_pounds = 130 
height_m = total_height_inches* 0.0254
weight_kg = weight_pounds * 0.453592
BMI_calculator = weight_kg/height_m ** 2
print(f"your BMI is {round(BMI_calculator,2)} ")
