import fresh_tomatoes
import media

toy_story=media.Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar=media.Movie("Avatar",
                    "A marine on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock=media.Movie("School of Rock",
                           "Using rock music to learn",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                           "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille=media.Movie("Ratatouille",
                           "A rat is a chef in paris",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
                           "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris=media.Movie("Midnight in Paris",
                           "Going back in time to meet authors",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
                           "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games=media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,hunger_games]

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.valid_ratings)
