from Laptop import Laptop

ordinary = Laptop()

budget = Laptop(1.1, 2, "Asus")

gaming = Laptop(4.0, 32, "DELL", "Discrete", 8, "OLED")

print(gaming)
print(budget)
print(ordinary)

Laptop.print_static_field()
