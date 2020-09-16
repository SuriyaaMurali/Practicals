from taxi import Taxi

# Create taxi
taxi_1 = Taxi("Prius 1", 100)
print(taxi_1)

# Drive 40km
taxi_1.drive(40)
print(taxi_1)

# Start a new fare
taxi_1.start_fare()
taxi_1.drive(100)
print(taxi_1)

#Current fare price
print(taxi_1.get_fare())