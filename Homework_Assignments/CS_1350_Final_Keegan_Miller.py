#Problem 1
print("PROBLEM 1")
loans = {
    "alice": {"fiction": [14, 21, 7], "history": [10]},
    "bob": {"fiction": [3, 5], "science": [28, 14]},
    "carol": {"science": [21, 21, 21], "history": [7, 14]}, 
    "dave": {"fiction": [30, 30, 30], "poetry": [2]},
}

def loan_summary(loans):
    patron_totals = {}
    genre_totals = {}
    genre_counts = {}
    longest_per_genre = {}
    longest_days = {}

    for patron, genres in loans.items():
        total_books = 0

        for genre, days_list in genres.items():
            total_books += len(days_list)

            if genre not in genre_totals:
                genre_totals[genre] = 0
                genre_counts[genre] = 0
                longest_days[genre] = 0

            genre_totals[genre] += sum(days_list)
            genre_counts[genre] += len(days_list)

            patron_longest = max(days_list)

            if patron_longest > longest_days[genre]:
                longest_days[genre] = patron_longest
                longest_per_genre[genre] = patron

        patron_totals[patron] = total_books

    genre_avg_days = {}

    for genre in genre_totals:
        genre_avg_days[genre] = genre_totals[genre] / genre_counts[genre]

    return {
        "patron_totals": patron_totals,
        "genre_avg_days": genre_avg_days,
        "longest_per_genre": longest_per_genre
    }

result = loan_summary(loans)
print(result)

#Problem 5
print("PROBLEM 5")
def reverse_words(s):
    words = s.split()

    def helper(lst):
        # BASE CASE
        if len(lst) <= 1:
            return lst

        # recursive step: last word + reverse of remaining words
        return [lst[-1]] + helper(lst[:-1])

    reversed_list = helper(words)
    result = " ".join(reversed_list)
    print(result)

reverse_words("hello world")
reverse_words("the quick brown fox")
reverse_words("python")
reverse_words("")
reverse_words("a b c d e")
reverse_words("CS 1350 is fun")