# This is a mixtape mixer which will randomly print out 5-10 different tracks
# to listen to for any given day of the week.
import random
print("Welcome to the Daily Mixtape Maker!\n")
# Creates input string for someone's favorite songs,
# then splits songs into list items.
song_string = input("What are your favorite songs? Include a minimum of 10 "
                    "songs. Separate each song with a comma.\n")
songs = song_string.split(", ")
# Creates lists for days of the week and music genre.
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"]
music_genre = ["Rock", "HipHop", "Pop", "Alternative", "Electronica",
               "Classical"]
# Creates a for loop for each day of the week.
for day in week:
    print(f"\nToday is {day}!\n")
# Creates if if/elif statements for different outcomes for Sunday & Thursday.
# Generates a random choice of a new genre on Sunday from music_genre list
# and ends the program since Sunday is at the end of the week list.
    if day == "Sunday":
        random_genre = random.choice(music_genre)
        print(f"Time for you to try a new artist! "
              f"How about listening to new music in {random_genre}.")
        print("\nThanks for using the Daily Mixtape Mixer!"
              " See you next week!")
        break
    elif day == "Thursday":
        print("It's Throwback Thursday! Find an artist you haven't listened to"
              " in awhile and give them a listen!")
    else:
        # Creates the playlist size by randomly choosing value
        # between 5 and 10.
        playlist_size = random.randint(5, 10)
        time = int(input("What time is it? Omit colon (e.g., 1230).\n"))
        ampm = input("Is it am or pm?\n").lower()
        if ampm == "pm":
            time += 1200
        elif ampm == "am" and time >= 1200 and time <= 1259:
            time -= 1200
        mood = input("What is your mood right now? "
                     "Happy, sad, or tired?\n").lower()
# Randomly samples the list of songs based on playlist size.
        mixtape = random.sample(songs, playlist_size)
# Creates nested if statements based on the time and mood.
        if mood == "happy" and time <= 1200:
            print(f"Keep those positive thoughts going for the morning! "
                  f"Here's your curated list for the morning:\n{mixtape}")
        elif mood == "happy" and time > 1200:
            print(f"You've had a great day! "
                  f"Enjoy this curated list for the afternoon:\n {mixtape}")
        elif mood == "sad" and time <= 1200 or "tired" and time <= 1200:
            print(f"It's time to get pumped! Here's your tracks to start "
                  f"the day off right:\n {mixtape}")
        elif mood == "sad" and time > 1200 or mood == "tired" and time > 1200:
            print(f"It's been a tough day! But here's some tracks to lift "
                  f"up your afternoon:\n {mixtape}")
        else:
            print("Error. Please try again!")
            break
# Asks if person wants to see the next day. If so, then the for loop continues
# to next day, otherwise the program terminates.
    next_day = input("\nDo you want to see tomorrow's "
                     "recommendations? Y/N.\n").lower()
    if next_day == "n":
        print("Thank you for using the Daily Mixtape Mixer!")
        break
