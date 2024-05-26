class Article:
  """Represents an article written by an author for a magazine."""

  all = []  # Class list to store all articles (assuming unique titles)

  def __init__(self, title, magazine):
    if not isinstance(title, str):
      raise TypeError("Article title must be a string")
    self.title = title
    self.magazine = magazine
    Article.all.append(self)

  # Enforce immutability for title (optional)
  # @property
  # def title(self):
  #   return self._title

  # @title.setter
  # def title(self, value):
  #   if not isinstance(value, str):
  #     raise TypeError("Article title must be a string")
  #   self._title = value

  @classmethod
  def get_all_articles(cls):
    return cls.all  # Return the list of all articles

class Author:
  """Represents an author who writes articles for magazines"""

  def __init__(self, name):
    if not isinstance(name, str):
      raise TypeError("Author name must be a string")
    self.name = name
    self.articles = []  # List to store articles written by the author

  def add_article(self, magazine, title):
    """Creates a new article for the given magazine and associates it with the author."""
    new_article = Article(title, magazine)
    self.articles.append(new_article)
    return new_article

  def articles(self):
    """Returns a list of articles written by the author."""
    return self.articles

  # Implement methods for managing topics (if applicable)
  # ...

class Magazine:
  """Represents a magazine that publishes articles."""

  def __init__(self, name, category):
    if not isinstance(name, str):
      raise TypeError("Magazine name must be a string")
    if not isinstance(category, str):
      raise TypeError("Magazine category must be a string")
    self.name = name
    self.category = category
    self.articles = []  # List to store articles published in the magazine
    self.contributors = []  # List to store authors who contributed to the magazine

  def articles(self):
    """Returns a list of articles published in the magazine."""
    return self.articles

  def contributors(self):
    """Returns a list of authors who contributed to the magazine."""
    return self.contributors

  def add_article(self, author, article):
    """Associates an existing article with the magazine and adds the author as a contributor (if not already present)."""
    if article not in self.articles:
      self.articles.append(article)
    if author not in self.contributors:
      self.contributors.append(author)

  def add_contributor(self, author):
    """Adds an author as a contributor to the magazine (if not already present)."""
    if author not in self.contributors:
      self.contributors.append(author)

# Sample usage
author1 = Author("John Doe")
magazine1 = Magazine("Tech Times", "Technology")

article1 = author1.add_article(magazine1, "AI in the Future")
magazine1.add_article(author1, article1)  # Associate existing article with magazine
magazine1.add_contributor(author1)

# Access articles and contributors
print(f"Articles by {author1.name}: {author1.articles()}")
print(f"Contributors to {magazine1.name}: {magazine1.contributors()}")

# Test functionality using your test suite (not included here)
