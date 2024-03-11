class Article:
     def __init__(self, author, magazine, title):
         
        if not isinstance(title, str):
            raise ValueError("Article title must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
         
        self.title = title
        self.author = author
        self.magazine = magazine
        
class Author:
     def __init__(self, name):
         if not isinstance(name, str):
             raise ValueError("Author's name must be a str")
         if not name:
             raise ValueError("Author's name must be longer than 0 characters")
         self.name = name

     def articles(self, title):
         self.title = title

     def magazines(self):
         pass

     def add_article(self, magazine, title):
         self.magazine = magazine
         self.title = title

     def topic_areas(self):
         pass

class Magazine:
     def __init__(self, name, category):
         if not isinstance(name, str):
             raise ValueError ("Magazine name must be of type str")
         if len(name) <2 or len(name) > 16:
             raise ValueError("Name must be between 2 and 16 characters")
         self.name = name

         if not isinstance(category,str):
             raise TypeError("Category must be a string")
         if not category:
             raise ValueError("Category must contain at least one character")
         self.category = category

     def articles(self):
         pass

     def contributors(self):
         pass

     def article_titles(self):
         pass

     def contributing_authors(self):
         pass