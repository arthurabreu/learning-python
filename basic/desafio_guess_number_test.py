import unittest
from unittest.mock import patch
import desafio_guess_number as game

class TestGame(unittest.TestCase):
    # Verifica se o número gerado está entre 1 e 100
    def test_generate_random_number(self):
        for _ in range(100):
            num = game.generate_random_number()
            self.assertTrue(1 <= num <= 100)

    # Simula uma partida onde o usuário acerta na primeira tentativa
    def test_compare_numbers_correct_guess(self):
        game.number_of_tries = 1
        with patch('desafio_guess_number.generate_random_number') as mock_generate_random_number:
            mock_generate_random_number.return_value = 42 

        with patch('desafio_guess_number.reset_game') as mock_reset_game:
            game.compare_numbers(42)
            mock_reset_game.assert_called_once()

    # Simula uma partida onde o usuário erra todas as tentativas
    def test_compare_numbers_incorrect_guess(self):
        game.number_of_tries = 5

        with patch('builtins.print') as mock_print:
            with patch('desafio_guess_number.reset_game') as mock_reset_game:
                game.compare_numbers(42)
                mock_print.assert_any_call('Você esgotou suas tentativas!')
                mock_reset_game.assert_called_once()

    def test_reset_game_play_again(self):
        game.reset_game()
        self.assertEqual(game.number_of_tries, 5)

        with patch('builtins.input', return_value='s'):
            with patch('desafio_guess_number.start_game') as mock_start_game:
                game.reset_game()
                mock_start_game.assert_called_once()

    def test_start_game(self):
        with patch('desafio_guess_number.generate_random_number') as mock_generate_random_number:
            mock_generate_random_number.return_value = 42 

            with patch('desafio_guess_number.compare_numbers') as mock_compare_numbers:
                game.start_game()
                mock_compare_numbers.assert_called_once_with(42)

if __name__ == '__main__':
    unittest.main()