import spacy
nlp = spacy.load("en_core_web_md")


def similar_movie(description):
    """ Function finds similarity for each movie with description.
    Creates a dictionary with similarity as a key and the title of the movie as a value.
    Finds max vulue of similarity and returns respective movie. """
    movie_similarirty = {}
    nlp_description = nlp(description)
    for movie in movies:
        similarity = nlp(movie).similarity(nlp_description)
        movie_similarirty[similarity] = movie

    max_similarity = max(movie_similarirty.keys())
    return movie_similarirty[max_similarity]

movies = []
with open("movies.txt", "r", encoding="utf-8") as f1:
    for line in f1:
        movies.append(line.strip("\n"))


description = """Will he save their world or destroy it?
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk 
into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into 
slavery and trained as a gladiator."""

print(similar_movie(description))
    