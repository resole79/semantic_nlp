# Import
import spacy

# Call method to load english language model
nlp = spacy.load("en_core_web_md")


# Function
def similar_movie_by_description(sentence_description):
    # Declare Variable
    file = "movies.txt"
    dissimilarity_grade = 0
    title_of_similar_movie = ""

    sentence_description_nlp = nlp(sentence_description)

    # Open file 'movies.txt'
    with open(file) as movie_file:

        # "for" cycle to read all movie
        for movies in movie_file:
            # Split movie in two variable title and description
            title_movie, description_movie = movies.split(" :")
            description_movie_nlp = nlp(description_movie)
            # Find the similarity grade between description and movie description inside file txt
            similarity_grade = sentence_description_nlp.similarity(description_movie_nlp)

            # "if" condition to check higher grade of similarity
            if similarity_grade > dissimilarity_grade:
                dissimilarity_grade = similarity_grade
                title_of_similar_movie = title_movie.strip()
            
    return title_of_similar_movie


# description movie
description = "Will he save their world or destroy it?"
description += "When the Hulk becomes too dangerous for the Earth, the Illuminati"
description += "trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace."
description += "Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Call the 'find_similar_movie' function with the given movie description and store the returned movie title.
similar_movie = similar_movie_by_description(description)

# Print out title of the similar movie by description
print(f"The most similar movie to 'Planet Hulk' is: {similar_movie}")
