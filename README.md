# Assignment 8

This project processes Pokémon data from a CSV file and creates a new CSV file with selected information about each Pokémon.

## Files

- `assignment8.py`: The main script that reads Pokémon data, processes it, and writes the processed data to a new CSV file.
- `pokemon_data.csv`: The input CSV file containing Pokémon data.

## Functions

### `open_pokemon_data()`

Reads the Pokémon data from `pokemon_data.csv` and returns it as a list of lists.

- **Returns**: A list of lists where each inner list represents a row of data from the CSV file.

### `pokemon_csv()`

Processes the Pokémon data to create a tuple for each Pokémon with the `dexnum`, `name`, `generation`, and `species`, and writes these tuples into a new CSV file `pokemon_tuples.csv`.

- **Returns**: A success message indicating that the file was created successfully.

## Usage

1. Ensure that `pokemon_data.csv` is in the same directory as `assignment8.py`.
2. Run the script `assignment8.py` to process the data and create the new CSV file.
