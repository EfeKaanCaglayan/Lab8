from book import Book
from article import Article
from podcast import Podcast
from file_manager import write_archive_data, read_archive_data

# İçerikler oluşturuluyor
items = [
    Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
    Book("B002", "Python Basics", 2021, "John Smith", 300),
    Article("A101", "Quantum Computing", 2022, "Nature", "10.1234/qc567"),
    Article("A102", "AI Ethics", 2017, "AI Journal", "10.5678/ethics42"),
    Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45),
    Podcast("P302", "History Unfolded", 2015, "Mark Twain", 60)
]

# Dosyaya yaz ve sonra tekrar yükle
write_archive_data(items, "output_archive.txt")
restored = read_archive_data("output_archive.txt")

print("=== All Items ===")
for item in restored:
    print(item)

print("\n=== Recent (Last 5 Years) ===")
for item in restored:
    if item.published_within_last_n_years(5):
        print(item)

print("\n=== Articles with DOI '10.1234' ===")
for item in restored:
    if isinstance(item, Article) and item.doi_code.startswith("10.1234"):
        print(item)
