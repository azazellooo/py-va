import wolframalpha
import wikipedia
import os


def get_wolframs_answer(query):
    client = wolframalpha.Client(os.environ.get('WOLFRAMALPHA_TOKEN'))
    return next(client.query(query).results).text


def get_wikis_answer(query):
    return wikipedia.summary(query, sentences=2)
