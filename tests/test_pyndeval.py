import unittest
import pyndeval
from pyndeval import SubtopicQrel, ScoredDoc


class TestPyndeval(unittest.TestCase):

    def test_basic(self):
        # provide qrels as a list of tuples
        qrels = [
            SubtopicQrel("0", "a", "A", 1),
            SubtopicQrel("0", "b", "B", 1),
            SubtopicQrel("0", "b", "D", 1),
            SubtopicQrel("0", "c", "C", 1),
        ]

        # provide run as a list of tuples
        run = [
            ScoredDoc("0", "A", 9.3),
            ScoredDoc("0", "D", 8.4),
            ScoredDoc("0", "E", 8.1), # not in qrels
            ScoredDoc("0", "B", 7.6),
            # C not retrieved
        ]

        results = pyndeval.ndeval(qrels, run)
        expected = {'0': {
          'ERR-IA@5': 0.3933,
          'ERR-IA@10': 0.3907,
          'ERR-IA@20': 0.3907,
          'ERR-IA@50': 0.3907,
          'ERR-IA@100': 0.3907,
          'nERR-IA@5': 0.8297,
          'nERR-IA@10': 0.8297,
          'nERR-IA@20': 0.8297,
          'nERR-IA@50': 0.8297,
          'nERR-IA@100': 0.8297,
          'alpha-DCG@5': 0.4052,
          'alpha-DCG@10': 0.3998,
          'alpha-DCG@20': 0.3997,
          'alpha-DCG@50': 0.3997,
          'alpha-DCG@100': 0.3997,
          'alpha-nDCG@5': 0.7868,
          'alpha-nDCG@10': 0.7868,
          'alpha-nDCG@20': 0.7868,
          'alpha-nDCG@50': 0.7868,
          'alpha-nDCG@100': 0.7868,
          'NRBP': 0.3906,
          'nNRBP': 0.8620,
          'MAP-IA': 0.5000,
          'P-IA@5': 0.2000,  # (0.4 + 0.2 + 0)/3 = 0.2
          'P-IA@10': 0.1000, # (0.2 + 0.1 + 0)/3 = 0.1
          'P-IA@20': 0.0500, # (0.1 + 0.05 + 0)/3 = 0.05
          'P-IA@50': 0.0200, # (2/50 + 1/50 + 0)/3 = 0.02 
          'P-IA@100': 0.0100,# (2/100 + 1/100 + 0)/3 = 0.01 
          'strec@5': 0.6666,
          'strec@10': 0.6666,
          'strec@20': 0.6666
          'strec@50': 0.6666
          'strec@100': 0.6666
        }}
        for measure, value in expected['0'].items():
            self.assertAlmostEqual(results['0'][measure], value, delta=1e-4)



if __name__ == '__main__':
    unittest.main()
