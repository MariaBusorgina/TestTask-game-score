import unittest

from game import get_score


class TestGetScore(unittest.TestCase):
    """Класс для тестирования функции get_score"""

    def setUp(self):
        self.game_stamps = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 5, "score": {"home": 1, "away": 0}},
            {"offset": 10, "score": {"home": 1, "away": 1}},
            {"offset": 15, "score": {"home": 2, "away": 1}}
        ]

    def test_offset_equal_to_first_stamp(self):
        """Проверка счета на первую фиксацию времени"""
        home_score, away_score = get_score(self.game_stamps, 0)
        self.assertEqual(home_score, 0)
        self.assertEqual(away_score, 0)

    def test_offset_equal_to_last_stamp(self):
        """Проверка счета на последнюю фиксацию времени"""
        home_score, away_score = get_score(self.game_stamps, 15)
        self.assertEqual(home_score, 2)
        self.assertEqual(away_score, 1)

    def test_offset_between_stamps(self):
        """Проверка счета для момента времени, находящегося между двумя фиксациями времени игры"""
        home_score, away_score = get_score(self.game_stamps, 7)
        self.assertEqual(home_score, 1)
        self.assertEqual(away_score, 0)

    # хз
    def test_offset_beyond_limit(self):
        """Проверка обработки ситуации, когда смещение выходит за пределы списка фиксаций времени игры"""
        result = get_score(self.game_stamps, 16)
        self.assertEqual(result, f"The score is {self.game_stamps[-1]['score']['home']}:{self.game_stamps[-1]['score']['away']} at the end of the game")

    def test_offset_negative(self):
        """Проверка обработки отрицательного смещения"""
        result = get_score(self.game_stamps, -1)
        self.assertEqual(result, "Invalid offset. Offset should be a number greater than or equal to 0.")

    def test_offset_float(self):
        """Проверка обработки вещественного смещения"""
        result = get_score(self.game_stamps, 1.5)
        self.assertEqual(result, "Invalid offset. Offset should be a number greater than or equal to 0.")

    def test_offset_valid(self):
        """Проверка типов данных возвращаемых значений"""
        home_score, away_score = get_score(self.game_stamps, 5)
        self.assertIsInstance(home_score, int)
        self.assertIsInstance(away_score, int)

    def test_offset_no_numeric(self):
        """Проверка обработки строкового смещения"""
        result = get_score(self.game_stamps, 'invalid')
        self.assertEqual(result, "Invalid offset. Offset should be a number greater than or equal to 0.")


if __name__ == 'main':
    unittest.main()