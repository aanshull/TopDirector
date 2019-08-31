import csv
from collections import defaultdict, namedtuple

# Global
MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 10
MIN_MOVIES = 3
MIN_YEAR = 1970
Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    directors = defaultdict(list)
    Movie = namedtuple("movie", ('movie_title', 'title_year', 'imdb_score'))
    with open(MOVIE_DATA, encoding="utf8") as f:
        movies = csv.DictReader(f)
        for movie in movies:
            directors[movie['director_name']].append(
                Movie(movie['movie_title'], movie['title_year'], movie['imdb_score']))
    return directors


def get_average_scores(directors):
    nominated_directors = {}
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            nominated_directors[(director, _calc_mean(movies))] = movies
    return nominated_directors


def _calc_mean(movies):
    scores = [float(movie.imdb_score) for movie in movies]
    return round(sum(scores) / len(scores), 1)


def print_results(directors):
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    report = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)
    for i in range(NUM_TOP_DIRECTORS):
        print(fmt_director_entry.format(counter=i + 1, director=report[i][0][0], avg=report[i][0][1]))
        print(sep_line)
        for movie in report[i][1]:
            x = fmt_movie_entry.format(year=movie.title_year, title=movie.movie_title, score=movie.imdb_score)
            print(x)


def main():
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
