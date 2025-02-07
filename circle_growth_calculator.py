import math

def calculate_circle_properties(radius, increase_percentage, iterations):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    
    print(f"Initial Circumference: {circumference:.4f} km")
    print(f"Initial Area: {area:.4f} km²\n")
    
    for i in range(1, iterations + 1):
        circumference *= (1 + increase_percentage / 100)
        area *= (1 + increase_percentage / 100)
        print(f"Iteration {i}:")
        print(f"Circumference: {circumference:.4f} km")
        print(f"Area: {area:.4f} km²\n")

if __name__ == "__main__":
    radius = float(input("Enter the initial radius (km): "))
    increase_percentage = float(input("Enter the percentage increase per iteration: "))
    iterations = int(input("Enter the number of iterations: "))
    
    calculate_circle_properties(radius, increase_percentage, iterations)
