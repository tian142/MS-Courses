# We are going to write some code to display play counts for songs stored in a text file using a dictionary

# This function will create and return the completed dictionary


def create_playcounts_dictionary(filename):

    # Read in the file contents and store to a list

    file_lines = open(filename, "r").readlines()

    # make an empty dictionary and save it to a variable
    # we are going to build up the keys and values from the file data
    play_count_dictionary = {}
    # Loop through the lines, parse, and store
    for line in file_lines:
        split_line_list = line.rstrip().split(",")

        # get the song name as the key and the play count as the value
        song_name = split_line_list[0]
        play_count = split_line_list[1]

        # Adds to dictionary
        play_count_dictionary[song_name] = int(play_count)

    return play_count_dictionary


print(create_playcounts_dictionary("data.txt"))
