from unittest.mock import patch
import app


def test_addition():
    # Мокапінг вводу користувача
    with patch("builtins.input", return_value="1"):
        assert app.add(2, 3) == 5
        assert app.add(-1, 1) == 0
        assert app.add(0, 0) == 0
        assert app.add(-1, -1) == -2


if __name__ == "__main__":
    pytest.main()

