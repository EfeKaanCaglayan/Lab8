from archive_item import ArchiveItem

class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal_name, doi_code):
        super().__init__(uid, title, year)
        self.journal_name = journal_name
        self.doi_code = doi_code

    def __str__(self):
        return f"Article -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.journal_name}, DOI: {self.doi_code}"
