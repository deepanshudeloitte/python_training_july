import pandas as pd


data = pd.read_csv('book_data.csv')
books = data['Book'].tolist()
prices = data['Price'].tolist()


threshold = 50

# Filter: Identifing books priced higher than the threshold
filtered_books = [book for book, price in zip(books, prices) if price > threshold]

# Reduce: Calculate total revenue from the sales of filtered books
total_revenue = sum(price for price in prices if price > threshold)

# Zip: list of tuples containing book titles and prices
book_price_tuples = list(zip(books, prices))

# Printing the results
print("Filtered Books:", filtered_books)
print("Total Revenue:", total_revenue)
print("Book-Price Tuples:", book_price_tuples)
