from book import Book
from article import Article
from podcast import Podcast

def write_archive_data(item_list, path):
    with open(path, 'w') as f:
        for item in item_list:
            if isinstance(item, Book):
                f.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.page_count}\n")
            elif isinstance(item, Article):
                f.write(f"Article,{item.uid},{item.title},{item.year},{item.journal_name},{item.doi_code}\n")
            elif isinstance(item, Podcast):
                f.write(f"Podcast,{item.uid},{item.title},{item.year},{item.presenter},{item.minutes}\n")


def read_archive_data(path):
    objects = []
    with open(path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            item_type = parts[0]
            data = parts[1:]
            if item_type == "Book":
                objects.append(Book(*data))
            elif item_type == "Article":
                objects.append(Article(*data))
            elif item_type == "Podcast":
                objects.append(Podcast(*data))
    return objects
