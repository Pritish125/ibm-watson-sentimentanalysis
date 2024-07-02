from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
        
        r1 = sentiment_analyzer("I love working with Python")["label"]
        self.assertEqual(r1, "SENT_POSITIVE")

        r2 = sentiment_analyzer("I hate working with Pyhton")["label"]
        self.assertEqual(r2, "SENT_NEGATIVE")

        r3 = sentiment_analyzer("I am neutral on Python")["label"]
        self.assertEqual(r3, "SENT_NEUTRAL")


unittest.main()