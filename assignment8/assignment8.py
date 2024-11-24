#Write a function that creates a tuple for each Pokemon with the 
#dexnum, name, generation, and species and writes it into a CSV file.

def open_pokemon_data(): #function to open the pokemon data file
    """
    This function opens the pokemon_data.csv file and reads the contents of the file.
    Returns the data in a list of lists.
    """
    try:
        with open("pokemon_data.csv", "r") as file:

            contents = file.read() #reading the contents of the file
            lines = contents.splitlines() #splitting the contents by lines
     #splitting the lines by commas and saving them to a list of columns for my sanity
        columns = [line.split(",") for line in lines] 
        data = columns #sets the data to the columns but will still include the header for later on

        return data #returns the data
    except FileNotFoundError: #if the file is not found it will print an error message
        print("Error: The file 'pokemon_data.csv' was not found.")

def pokemon_csv():
    """
    This function will create a tuple for each Pokemon with the dexnum, name, generation, and species and write it into a CSV file.
    Fruitful function just to return a success message.
    """
    try:
        pokemon_list = [] #creates an empty list to store the pokemon tuples

        pokemon_data = open_pokemon_data() #uses the open_pokemon_data function to get the data

        header = pokemon_data[0] #gets the header of the file
        pokemons = pokemon_data[1:]

        dexnum_index = header.index("dexnum") #gets the index of the DexNum column
        name_index = header.index("name") #gets the index of the Name column
        generation_index = header.index("generation") #gets the index of the Generation column
        species_index = header.index("species") #gets the index of the Species column

        for i in range(len(pokemons)): 
            #loops through the pokemon data getting dexnum, name, generation, and species and strips them of any whitespace
            dexnum = pokemons[i][dexnum_index].strip()
            name = pokemons[i][name_index].strip()
            generation = pokemons[i][generation_index].strip()
            species = pokemons[i][species_index].strip()
            pokemon_list.append((dexnum, name, generation, species))

        #creates a CSV file with the dexnum, name, generation, and species of the pokemon
        file_name = "pokemon_tuples.csv"
        with open(file_name, "w") as file:
            file.write("dexnum,name,generation,species\n")
            for pokemon in pokemon_list:
                file.write(",".join(pokemon) + "\n")
        #prints a message if the file was successfully created
        return print("Successfully created the file 'pokemon_tuples.csv'.")

    except FileNotFoundError:
        print("Error: The file 'pokemon_data.csv' was not found.")


pokemon_csv() #calls the function to create the CSV file with the dexnum, name, generation, and species of the pokemon