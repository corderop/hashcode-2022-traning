from queue import PriorityQueue
from typing import List
from io_files.dataclass import ProblemData, Ride, SolutionData, Vehicle

def create_priority_queue(rides: List[Ride]):
    queue = PriorityQueue()
    for ride in rides:
        queue.put(ride)
        
    return queue

def get_distance_between_points(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1]) 

def get_maximum_ride_steps(ride: Ride):
    return ride.latest_finish - ride.earliest_start

def is_suitable_for_bonus(vehicle: Vehicle, ride: Ride):
    return vehicle.position == ride.start and vehicle.step == ride.earliest_start 

def get_distance_of_ride_for_a_vehicle(vehicle: Vehicle, ride: Ride):
    distance_to_start = get_distance_between_points(vehicle.position, ride.start)
    distance_to_finish = get_distance_between_points(ride.start, ride.finish) 
    distance = distance_to_start + distance_to_finish
    
    return distance

def calculate_points_from_ride(vehicle: Vehicle, ride: Ride, bonus: int):
    points = 0
    
    if is_suitable_for_bonus(vehicle, ride):
        points += bonus
     
    distance = get_distance_of_ride_for_a_vehicle(vehicle, ride)
    max_ride_steps = get_maximum_ride_steps(ride)
    
    if distance > max_ride_steps:
        return 0
    
    return points + distance

def get_best_vehicle_for_a_ride(vehicles: List[Vehicle], ride: Ride, bonus: int):
    best_points = 0
    best_vehicle = 0
    
    for index, vehicle in enumerate(vehicles):
        ride_points = calculate_points_from_ride(vehicle, ride, bonus)
    
        if ride_points != 0 and ride_points > best_points:
            best_vehicle = index
            best_points = ride_points
    
    return best_vehicle, best_points

def asign_ride_to_vehicle(ride: Ride, vehicle: Vehicle):
    steps_to_make = get_distance_of_ride_for_a_vehicle(vehicle, ride)
    
    vehicle.position = ride.finish
    vehicle.rides.append(ride.idx)
    vehicle.step += steps_to_make
    return vehicle
    

def process_data(data: ProblemData, type: str) -> SolutionData:
    vehicles = [Vehicle(position=[0,0], step=0, rides=[]) for i in range(data.vehicles)]
    queue_rides = create_priority_queue(data.rides) # O(n*log(n))
    total_points = 0
    
    # O(n*m)
    while not queue_rides.empty():
        ride = queue_rides.get()
        best_vehicle, points = get_best_vehicle_for_a_ride(vehicles, ride, data.bonus)
    
        if points != 0:    
            # Update state of vehicle
            steps_to_make = get_distance_of_ride_for_a_vehicle(vehicles[best_vehicle], ride)
            vehicles[best_vehicle].position = ride.finish
            vehicles[best_vehicle].rides.append(ride.idx)
            vehicles[best_vehicle].step += steps_to_make
        
            total_points += points

    return SolutionData(points=total_points, vehicles=vehicles)