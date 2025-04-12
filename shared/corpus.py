import os
import re
from shared.constants import *
from shared.utils import remove_punctuation


# def load_corpus(dir_path: str) -> list[list[str]]:
#     """
#     Load a text corpus from .txt files, splitting each file into chapters.

#     Returns:
#         List[List[str]]: Each inner list contains chapter texts from one file.
#     """
#     corpus = []
#     files = sorted([os.path.join(dir_path, f) for f in os.listdir(dir_path)])
#     for file in files:
#         with open(file, 'r') as f:
#             text = f.read().strip()
#             text = re.sub(r'\n+', ' ', text)
#             split_text = re.split(PATTERN_CHAPTER_LINE, text)
#             corpus.append(split_text)
#     return corpus


class Chapter:

    def __init__(self, text: str) -> None:
        self.text = text.strip()


class Book:

    def __init__(self, text: str) -> None:
        self.chapters: list[Chapter] = self.__get_chapters(text)

    def __get_chapters(self, text: str):
        chapters: list[Chapter] = [
            Chapter(txt) for txt in re.split(PATTERN_CHAPTER_LINE, text) if txt
        ]
        return chapters

    @property
    def text(self):
        chapters = []
        for chapter in self.chapters:
            chapters.append(chapter.text)
        return ' '.join(chapters)


class Corpus:

    def __init__(
        self,
        dir_path: str,
        no_punct: bool = False,
        to_lower: bool = False,
    ) -> None:
        # preprocessing flags
        self.no_punct = no_punct
        self.to_lower = to_lower

        # data
        self.dir_path: str = dir_path
        self.files: list[str] = self.__get_files()
        self.books: list[Book] = self.__get_books()

    def __get_files(self) -> list[str]:
        files = [
            os.path.join(self.dir_path, f) for f in os.listdir(self.dir_path)
        ]
        return sorted(files)

    def __get_books(self) -> list[Book]:
        books: list[Book] = []
        for file in self.files:
            with open(file, 'r') as f:
                text = f.read().strip()
                text = re.sub(r"\s+", " ", text)
                if self.no_punct:
                    text = remove_punctuation(text)
                if self.to_lower:
                    text = text.lower()
                books.append(Book(text))
        return books

    @property
    def tokens(self):
        tokens = []
        for book in self.books:
            for chapter in book.chapters:
                tokens.extend(chapter.text.split())
        return tokens

    @property
    def text(self):
        chapters = []
        for book in self.books:
            for chapter in book.chapters:
                chapters.append(chapter.text)
        return ' '.join(chapters)
