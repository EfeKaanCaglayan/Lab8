from archive_item import ArchiveItem

class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, presenter, minutes):
        super().__init__(uid, title, year)
        self.presenter = presenter
        self.minutes = int(minutes)

    def __str__(self):
        return f"Podcast -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.presenter}, Duration: {self.minutes} mins"
