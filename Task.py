# This class manage the tasks
class Task:
    def __init__(self, title, description, expiration_date, priority):
        self.title = title
        self.description = description
        self.expiration_date = expiration_date
        self.priority = priority

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Expiration Date: {self.expiration_date}, Priority: {self.priority}"