# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle():  # base
    pass

class FlightVehicle(Vehicle):
    pass

class Starship(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

class GroundVehicle(Vehicle):
    pass

class car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass