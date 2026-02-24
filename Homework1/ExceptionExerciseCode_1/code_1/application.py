def display(data):
    print("Product details:")
    print(f"\tID: {data[0]}")
    print(f"\tName: {data[1]}")
    if len(data) == 7:
        print(f"\tAuthor: {data[5]}")
    print(f"\tCost price: {data[2]}")
    print(f"\tRetail price: {data[3]}")
    print(f"\tQuantity in stock: {data[4]}")
    if len(data) == 7:
        print(f"\tGenre(s): {data[6]}")


valid = False
count = 0
while not valid:
    print(f"Attempt {count}")
    if count == 4:
        print("You have 1 attempt left.")
    if count == 5:
        print("Shutting application down")
        quit()
    # Ask user to enter a filename
    filename = input("Please enter the inventory filename: ")
    try:
    #File not found
        with open(f"{filename}.txt", "r") as file_handle:

            # Read content of file in and store in a list of content
            for line in file_handle:
                line = line.strip()
                # the %% done exist
                components = line.split("%%")
                data = []
                try:
                    data.append(components[1])
                except IndexError as e:
                    print("Component not found")
                    quit()
                try:
                    data.append(components[2])
                except IndexError as e:
                    print("Component not found")
                    quit()

                try:
                    data.append(float(components[3]))
                except IndexError as e:
                    print("Component not found")
                    quit()

                try:
                    data.append(float(components[4]))
                except IndexError as e:
                    print("Component not found")
                    quit()

                try:
                    data.append(float(components[5]))
                except IndexError as e:
                    print("Component not found")
                    quit()

                if components[0] == "Book":
                    data.append(components[6])
                    #&& are mission
                    genres = components[7].split("&&")
                    data.append(genres)
                # Display data for this line
                display(data)
    except FileNotFoundError as e:
        count = count + 1
        print("File not found")
