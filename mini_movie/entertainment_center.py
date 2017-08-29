import media
import fresh_tomatoes

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/azyK_k52R1w")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

up_the_video_game = media.Movie("Up the video game",
                                "A story of an old man and a child",
                                "https://upload.wikimedia.org/wikipedia/en/4/47/Up_video_game.jpg",
                                "https://www.youtube.com/watch?v=TjatyyBMPEY")
# print(toy_story.storyline)
# print(toy_story.trailer_youtube_url)
# toy_story.show_trailer()

movies = [toy_story, avatar, up_the_video_game]
fresh_tomatoes.open_movies_page(movies)


