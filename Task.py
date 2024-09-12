# This class manage the tasks
class Task:
    def __init__(self, title, description, expiration_date, priority):
        self.title = title
        self.description = description
        self.expiration_date = expiration_date
        self.priority = priority

    def __str__(self):
        return f"\nTitle:\n\t {self.title},\n Description:\n\t {self.description},\n Expiration Date:\n\t {self.expiration_date},\n Priority:\n\t {self.priority}"