prices = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")


print("Select first service:")
service1 = str(input())
print("Select second service:\n")
service2 = str(input())

print("Davy's auto shop invoice\n")
if service1 or service2 == "-":
    if service1 == "-":
        print("Service 1: No service")
        print(f'Service 2: {service2}, ${prices[service2]}\n')
        print(f'Total: ${prices[service2]}')
    elif service2 == "-":
        print(f'Service 1: {service1}, ${prices[service1]}')
        print("Service 2: No service\n")
        print(f'Total: ${prices[service1]}')
if service1 and service2 != "-":

    print(f'Service 1: {service1}, ${prices[service1]}')
    print(f'Service 2: {service2}, ${prices[service2]}\n')
    total = prices[service1] + prices[service2]
    print(f'Total: ${total}')