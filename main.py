class BMW:
    def description(self):
        return "BMW: A German luxury vehicle known for its performance and technology."

    def top_speed(self):
        return "The top speed of a BMW can go up to 250 km/h."

class Ferrari:
    def description(self):
        return "Ferrari: An Italian sports car brand known for its speed and design."

    def top_speed(self):
        return "The top speed of a Ferrari can exceed 350 km/h."

# Function to demonstrate polymorphism
def car_details(car):
    print(car.description())
    print(car.top_speed())

# Example usage
if __name__ == "__main__":
    bmw_car = BMW()
    ferrari_car = Ferrari()

    print("Details of BMW:")
    car_details(bmw_car)
    print("\nDetails of Ferrari:")
    car_details(ferrari_car)
