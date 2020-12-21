# Wind Chill Chart
# Aiden Dow
# 11/2/2019 - Revised 12/21/2020

import datetime

def windChill(temp, velocity):
	"""Find the wind chill"""
	if velocity > 3:
		# This is the National Weather Service formula for calculating wind chill
		return 35.74 + (0.6215 * temp) - (35.75 * (velocity ** 0.16)) + (0.4275 * temp * (velocity ** 0.16))
	else:
		# This function only works for wind speeds higher than 3 mph 
		return temp

def main():
	print("Wind Chill Values Chart")

	print("-" * 79)
	print("\t\t\t\tTemperature")

	print("MPH|", end="\t")
	# Print the temperature key
	for temp in range(-20, 61, 10):
		print(temp, end="\t")
	print()
	
	print("---+" + "-" * 75)
	
	for wind in range(0, 51, 5):
		# Print the wind key
		print("{0:3}".format(wind), end="|\t")
		for temp in range(-20, 61, 10):
			# Fill in the chart
			print(round(windChill(temp, wind)), end="\t")
		print()

main()

print()
print("Aiden Dow")
print(datetime.datetime.now())
