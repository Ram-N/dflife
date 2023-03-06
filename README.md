

# Books Read Log (goodreads.py)

## Questions that can be asked
2. Last {n} books read for {genre} and their dates
3. How does my last 365 days compare to my ideal set of books for each year.
    Ex: 6 travel, 3 science etc. vs. what I'm actually reading
4. For a given genre, list the matching books in "to-read"

DONE
1. Number of Days since {genre} was last read


## Logic
- Read the input csv
- Create a list of Genres
- For each row (book), add it to the book dictionary 

## Data Structure

book_d = {'Science':[(title1, date1),(title1, date1),(title2, date2)]}
