class Laptop:
    number_of_notebooks = 0

    def __init__(self, cpu_frequency=2.5, ram=8, brand="HP"
                 , gpu_type="Integrated", core_count=4, screen_type="IPS"):
        self.cpu_frequency = cpu_frequency
        self.ram = ram
        self.brand = brand
        self.gpu_type = gpu_type
        self.core_count = core_count
        self.screen_type = screen_type
        Laptop.number_of_notebooks += 1

    def __str__(self):
        return ("Cpu Frequency: " + str(self.cpu_frequency) + "GHz\n" +
                "RAM size: " + str(self.ram) + "Gb\n" +
                "Brand: " + self.brand+"\nGPU type: " + self.gpu_type +
                "\nNumber of cores:" + str(self.core_count) +
                "\nScreen type: " + self.screen_type + "\n \n")

    def __del__(self):
        Laptop.number_of_notebooks -= 1
        print("Deletion is success")

    @staticmethod
    def print_static_field():
        print(Laptop.number_of_notebooks)
