import pytest
import requests
# phrase = input("Set a phrase: ")
class TestWordcount:
    def test_word_count(some):
        phrase = input("Set a phrase: ")

        word_count = len(phrase.split())

        assert word_count <15, f"фраза '{phrase}' состоит из 15 или более слов"
