from directors import get_movies_by_director, get_average_scores, _calc_mean, NUM_TOP_DIRECTORS, print_results

t = """
1. Sergio Leone                                         8.5
1984] Once Upon a Time in America                        8.4
1968] Once Upon a Time in the West                       8.6
1966] The Good, the Bad and the Ugly                     8.9
1964] A Fistful of Dollars                               8.0
2. Christopher Nolan                                    8.4
2012] The Dark Knight Rises                              8.5
2008] The Dark Knight                                    9.0
2014] Interstellar                                       8.6
2010] Inception                                          8.8
2005] Batman Begins                                      8.3
2002] Insomnia                                           7.2
2006] The Prestige                                       8.5
2000] Memento                                            8.5
3. Pete Docter                                          8.2
2009] Up                                                 8.3
2015] Inside Out                                         8.3
2001] Monsters, Inc.                                     8.1
4. Quentin Tarantino                                    8.2
2012] Django Unchained                                   8.5
2009] Inglourious Basterds                               8.3
2015] The Hateful Eight                                  7.9
2003] Kill Bill: Vol. 1                                  8.1
2004] Kill Bill: Vol. 2                                  8.0
1997] Jackie Brown                                       7.5
1994] Pulp Fiction                                       8.9
1992] Reservoir Dogs                                     8.4
5. Hayao Miyazaki                                       8.2
2008] Ponyo                                              7.7
2004] Howl's Moving Castle                               8.2
1997] Princess Mononoke                                  8.4
2001] Spirited Away                                      8.6
6. Milos Forman                                         8.1
1999] Man on the Moon                                    7.4
1984] Amadeus                                            8.3
1975] One Flew Over the Cuckoo's Nest                    8.7
7. Frank Capra                                          8.1
1946] It's a Wonderful Life                              8.6
1961] Pocketful of Miracles                              7.3
1938] You Can't Take It with You                         8.0
1939] Mr. Smith Goes to Washington                       8.2
1934] It Happened One Night                              8.2
8. Frank Darabont                                       8.0
2001] The Majestic                                       6.9
1999] The Green Mile                                     8.5
1994] The Shawshank Redemption                           9.3
2007] The Mist                                           7.2
9. Stanley Kubrick                                      8.0
1999] Eyes Wide Shut                                     7.3
1962] Lolita                                             7.7
1980] The Shining                                        8.4
1975] Barry Lyndon                                       8.1
1968] 2001: A Space Odyssey                              8.3
1962] Lolita                                             7.7
1964] Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb  8.5
10. Denis Villeneuve                                     8.0
2013] Prisoners                                          8.1
2015] Sicario                                            7.6
2010] Incendies                                          8.2"""
def test_director():
    directors = get_movies_by_director()

    assert 'Sergio Leone' in directors
    assert 'Andrew Stanton' in directors
    assert len(directors['Sergio Leone']) == 4
    assert len(directors['Peter Jackson']) == 12

    movies_sergio = directors['Sergio Leone']
    movies_nolan = directors['Christopher Nolan']
    movies_pete = directors['Pete Docter']
    assert _calc_mean(movies_sergio) == 8.5
    assert _calc_mean(movies_nolan) == 8.4
    assert _calc_mean(movies_pete) == 8.2

    directors = get_average_scores(directors)
    assert print_results(directors) is None

    expected_directors = ['Sergio Leone', 'Christopher Nolan', 'Pete Docter', 'Quentin Tarantino',
                          'Hayao Miyazaki', 'Milos Forman', 'Frank Capra', 'Frank Darabont',
                          'Stanley Kubrick', 'Denis Villeneuve']
    expected_avg_scores = [8.5, 8.4, 8.2, 8.2, 8.2, 8.1, 8.1, 8.0, 8.0, 8.0]
    expected_num_movies = [4, 8, 3, 8, 4, 3, 5, 4, 7, 3]
    assert NUM_TOP_DIRECTORS == len(expected_directors)
    report = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)
    for counter, (i, j, k) in enumerate(
            zip(expected_directors,
                expected_avg_scores, expected_num_movies)):
        assert report[counter][0] == (i, j)
        assert len(report[counter][1]) == k
        assert _calc_mean(report[counter][1]) == j

    return "tests pass"



if __name__ == '__main__':
    print(test_director())
