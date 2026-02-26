#Problem 1
print("Problem 1: Library Book System")
class Book:
    def __init__(self, title, author, total_pages, isbn):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.isbn = isbn
        self._current_page = 0

    @property
    def current_page(self):
        return self._current_page

    @property
    def progress(self):
        # Return percentage string like "45.0%"
        if self.total_pages == 0:
            return "0.0%"
        return f"{(self._current_page / self.total_pages * 100):.1f}%"

    def read(self, pages):
        # Advance current page by pages
        # Cap at total_pages
        # Print error if pages is not positive
        # Return new current page
        if pages <= 0:
            print("Error: Pages to read must be positive.")
            return self._current_page
        self._current_page += pages
        if self._current_page > self.total_pages:
            self._current_page = self.total_pages
        return self._current_page

    def reset(self):
        # Set _current_page back to 0
        self._current_page = 0

    def __str__(self):
        # Return formatted string
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {self.total_pages} pages"
class TextBook(Book):
    def __init__(self, title, author, total_pages, isbn, subject, edition):
        super().__init__(title, author, total_pages, isbn)
        self.subject = subject
        self.edition = edition
        self._highlights = {}

    def highlight(self, page, text):
        if page <= 0 or page > self.total_pages:
            print("Error: Page out of range.")
            return

        if page not in self._highlights:
            self._highlights[page] = []

        self._highlights[page].append(text)

    def get_highlights(self, page):
        return self._highlights.get(page, [])

    def __str__(self):
        return (
            f"'{self.title}' by {self.author} "
            f"(ISBN: {self.isbn}) - {self.total_pages} pages "
            f"(Subject: {self.subject}, Edition: {self.edition})"
        )
# Test your code
if __name__ == "__main__":
# --- Test Book ---
    print("=== Book Tests ===")
novel = Book("1984", "George Orwell", 328, "978-0451524935")
print(novel)
novel.read(50)
print(f"Current page: {novel.current_page}")
print(f"Progress: {novel.progress}")
novel.read(-10) # Should print error
novel.read(400) # Should cap at 328
print(f"Current page: {novel.current_page}")
print(f"Progress: {novel.progress}")
novel.reset()
print(f"After reset: page {novel.current_page}")
print("\n=== TextBook Tests ===")
# --- Test TextBook ---
cs_book = TextBook("Intro to Python", "Deitel", 880, "978-0135404676",
"Computer Science", 1)
print(cs_book)
cs_book.read(120)
print(f"Progress: {cs_book.progress}")
cs_book.highlight(45, "Dictionaries store key-value pairs")
cs_book.highlight(45, "Keys must be immutable")
cs_book.highlight(72, "Sets cannot contain duplicates")
cs_book.highlight(0, "Important note") # Should print error
print(f"Page 45 highlights: {cs_book.get_highlights(45)}")
print(f"Page 72 highlights: {cs_book.get_highlights(72)}")
print(f"Page 1 highlights: {cs_book.get_highlights(1)}")
