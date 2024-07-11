input = {
        "prompt":'''You will receive review commentary on a variety of movies from an IMDB database in a new line.  
                    Respond with just the output 'pos' if the sentiment in the comment describes the movie in a positive way, where the comment is happy, encouraging, expresses excitement, actively recommends the movie. 
                    Respond with just the output 'neg' if the sentiment in the comment describes the movie in a negative way, where the comment is critical, dismissive, actively dissuades future movie viewers.''',
        "system_prompt":"You are a linguistic expert who is reviewing movie review comments and you only know two words, 'pos' and 'neg'.",
}

sample_review_comment = 'this movie is bad'

def generate_prompt(input, movie_review_comment):
    prompt = f'{input}/n "the following comment is the movie review:"{movie_review_comment}'
    return prompt

sample_prompt = generate_prompt(input, sample_review_comment)

llama_prompt(sample_prompt)