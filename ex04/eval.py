class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        try:
            assert isinstance(coefs, list)
            assert isinstance(words, list)
            assert len(coefs) == len(words)
        except Exception:
            return -1
        else:
            try:
                return sum([coef * len(word)
                            for (coef, word) in zip(coefs, words)])
            except Exception:
                return -1

    @staticmethod
    def enumerate_evaluate(coefs, words):
        try:
            assert isinstance(coefs, list)
            assert isinstance(words, list)
            assert len(coefs) == len(words)
        except Exception:
            return -1
        else:
            try:
                return sum([coefs[i] * len(word)
                            for (i, word) in enumerate(words)])
            except Exception:
                return -1
