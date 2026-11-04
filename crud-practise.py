books = []


def find_book(book_id):
	return next((book for book in books if book["book_id"] == book_id), None)


def positive_number(prompt, kind):
	while True:
		try:
			value = kind(input(prompt).strip())
			if value > 0:
				return value
		except ValueError:
			pass
		print("Enter a positive number.")


def add_book():
	while True:
		try:
			book_id = int(input("Book ID: ").strip())
			if book_id <= 0:
				print("Book ID must be positive.")
			elif find_book(book_id):
				print("Book ID must be unique.")
			else:
				break
		except ValueError:
			print("Enter a valid Book ID.")

	books.append({
		"book_id": book_id,
		"book_name": input("Book Name: ").strip(),
		"author": input("Author Name: ").strip(),
		"category": input("Category: ").strip(),
		"price": positive_number("Price: ", float),
		"copies": positive_number("Number of Copies: ", int),
	})
	print("Book added successfully.")


def display_book(book):
	print(
		f"ID: {book['book_id']} | Name: {book['book_name']} | "
		f"Author: {book['author']} | Category: {book['category']} | "
		f"Price: {book['price']:g} | Copies: {book['copies']}"
	)


def view_books():
	if not books:
		print("No books available")
		return
	for book in books:
		display_book(book)


def update_book():
	try:
		book_id = int(input("Enter Book ID to update: ").strip())
	except ValueError:
		print("Invalid Book ID.")
		return
	book = find_book(book_id)
	if book is None:
		print("Book ID does not exist.")
		return

	print("Press Enter to keep the current value.")
	for key, label in (("book_name", "Book Name"), ("author", "Author Name"),
					   ("category", "Category")):
		value = input(f"{label} [{book[key]}]: ").strip()
		if value:
			book[key] = value

	for key, label, kind in (("price", "Price", float), ("copies", "Number of Copies", int)):
		while True:
			value = input(f"{label} [{book[key]}]: ").strip()
			if not value:
				break
			try:
				number = kind(value)
				if number > 0:
					book[key] = number
					break
			except ValueError:
				pass
			print("Enter a positive number.")
	print("Book updated successfully.")


def delete_book():
	try:
		book_id = int(input("Enter Book ID to delete: ").strip())
	except ValueError:
		print("Invalid Book ID.")
		return
	book = find_book(book_id)
	if book is None:
		print("Book ID does not exist.")
		return
	books.remove(book)
	print("Book deleted successfully.")


def search_book():
	query = input("Enter Book ID or Book Name: ").strip()
	try:
		book_id = int(query)
		matches = [book for book in books if book["book_id"] == book_id]
	except ValueError:
		matches = [book for book in books if query.casefold() in book["book_name"].casefold()]
	if not matches:
		print("No matching books found.")
		return
	for book in matches:
		display_book(book)


def main():
	actions = {
		"1": add_book,
		"2": view_books,
		"3": update_book,
		"4": delete_book,
		"5": search_book,
	}
	while True:
		print("\n========== LIBRARY MANAGEMENT ==========")
		print("1. Add New Book\n2. View All Books\n3. Update Book Details")
		print("4. Delete Book\n5. Search Book\n6. Exit")
		choice = input("Enter your choice: ").strip()
		if choice == "6":
			print("Exiting Library Management System.")
			break
		action = actions.get(choice)
		if action:
			action()
		else:
			print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
	main()