import pandas as pd


df = pd.read_csv("data/books/2023_03_04_goodreads_library_export.csv")

print(df.columns)
# print(df.info)

# ['Book Id', 'Title', 'Author', 'Author l-f', 'Additional Authors',
#        'ISBN', 'ISBN13', 'My Rating', 'Average Rating', 'Publisher', 'Binding',
#        'Number of Pages', 'Year Published', 'Original Publication Year',
#        'Date Read', 'Date Added', 'Bookshelves', 'Bookshelves with positions',
#        'Exclusive Shelf', 'My Review', 'Spoiler', 'Private Notes',
#        'Read Count', 'Owned Copies'],

useful_columns = ["Title", "Author", "Bookshelves"]

df = df[useful_columns]
drop_rows = df["Bookshelves"].str.contains("to-read").astype(bool)
print(drop_rows.value_counts())
print(drop_rows.dtype)
print(df[~drop_rows])
