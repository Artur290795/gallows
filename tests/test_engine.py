from app.engine import GallowEngine
from app.guess_result import GuessResult
from config import Config


class TestGallowEngine:
    def test_initial_state(self):
        engine = GallowEngine("тест")
        assert engine.word == "тест"
        assert engine.word_state == ["_", "_", "_", "_"]
        assert engine.attempts == Config.MAX_ATTEMPTS
        assert engine.used_letters == set()
        assert not engine.is_game_over
        assert not engine.is_success

    def test_correct_guess(self):
        engine = GallowEngine("кот")
        result = engine.guess("о")

        assert result == GuessResult.CORRECT
        assert engine.word_state == ["_", "о", "_"]
        assert "о" in engine.used_letters
        assert not engine.is_game_over
        assert engine.attempts == Config.MAX_ATTEMPTS

    def test_win(self):
        engine = GallowEngine("кот")
        engine.guess("к")
        engine.guess("о")
        result = engine.guess("т")
        
        assert result == GuessResult.WIN
        assert engine.word_state == ["к", "о", "т"]
        assert engine.is_game_over
        assert engine.is_success

    def test_incorrect_guess(self):
        engine = GallowEngine("кот")
        result = engine.guess("а")
        
        assert result == GuessResult.INCORRECT
        assert engine.attempts == Config.MAX_ATTEMPTS - 1
        assert "а" in engine.used_letters
        assert not engine.is_game_over

    def test_lose(self):
        engine = GallowEngine("кот")
        for letter in ["а", "б", "в", "г", "д", "е"]:
            result = engine.guess(letter)

        assert result == GuessResult.LOSE
        assert engine.attempts == 0
        assert engine.is_game_over
        assert not engine.is_success

    def test_already_used_letter(self):
        engine = GallowEngine("кот")
        engine.guess("о")
        result = engine.guess("о")
        assert result == GuessResult.ALREADY_USED

    def test_invalid_input(self):
        engine = GallowEngine("кот")
    
        assert engine.guess("1") == GuessResult.INVALID
        assert engine.guess("ко") == GuessResult.INVALID
        assert engine.guess("") == GuessResult.INVALID
        
