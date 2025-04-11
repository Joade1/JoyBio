measured_size = float(input("Enter measured size under microscope (in µm): "))
magnification = float(input("Enter magnification: "))
real_size = (measured_size / magnification) * 1000
print(f"The real size of the specimen is {real_size} µm")