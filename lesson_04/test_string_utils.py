from string_utils import StringUtils
import pytest

stringutils = StringUtils()


@pytest.mark.parametrize("input_string,expected", [
    ("skypro", "Skypro"),
    ("", ""),
    (" hello", " hello"),
])
@pytest.mark.positive
def test_capitalize_positive(input_string, expected):
    # Позитивные проверки
    assert stringutils.capitalize(input_string) == expected
    assert stringutils.capitalize("skypro") == "Skypro"
    assert stringutils.capitalize("hello world") == "Hello world"
    assert stringutils.capitalize("535")


@pytest.mark.parametrize("input_string,expected", [
    ("skypro", "Skypro"),
    ("", ""),
    (" hello", " hello"),
])
@pytest.mark.negative
def test_capitalize_negative(input_string, expected):

    # Негативные проверки
    assert stringutils.capitalize(input_string) == expected
    assert stringutils.capitalize("") == ""
    assert stringutils.capitalize(" ") == " "
    assert stringutils.capitalize("1234my") == "1234my"


@pytest.mark.parametrize("input_string,expected", [
    (" skypro", "skypro"),
    ("        skypro", "skypro"),
])
@pytest.mark.positive
def test_trim_positive(input_string, expected):
    # Позитивные проверки
    assert stringutils.trim(input_string) == expected
    assert stringutils.trim(" skypro") == "skypro"
    assert stringutils.trim("        skypro") == "skypro"


@pytest.mark.parametrize("input_string,expected", [
    ("sky pro", "sky pro"),
    ("...skypro", "...skypro"),
    ("skypro  ", "skypro  "),
    ("skypr o", "skypr o"),
    ("skyp ro", "skyp ro"),
    ("!#skypro", "!#skypro"),
    ("/tskypro", "/tskypro"),
])
@pytest.mark.negative
def test_trim_negative(input_string, expected):

    # Негативные проверки
    assert stringutils.trim(input_string) == expected
    assert stringutils.trim("sky pro") == "sky pro"
    assert stringutils.trim("...skypro") == "...skypro"
    assert stringutils.trim("skypro  ") == "skypro  "
    assert stringutils.trim("skypr o") == "skypr o"
    assert stringutils.trim("skyp  ro") == "skyp  ro"
    assert stringutils.trim("!#skypro") == "!#skypro"
    assert stringutils.trim("/tskypro") == "/tskypro"


@pytest.mark.parametrize("input_string, symbol, expected", [
    (" Skypro", "S", True),
    ("Skyeng", "g", True),
    ("Skyeng", "n", True)
])
@pytest.mark.positive
def test_contains_positive(input_string, symbol, expected):
    assert stringutils.contains(input_string, symbol) == expected
    # Позитивные проверки
    assert stringutils.contains("Skypro", "S") is True
    assert stringutils.contains("Skyeng", "g") is True
    assert stringutils.contains("Skyeng", "n") is True


@pytest.mark.parametrize("input_string, symbol, expected", [
    (" Skypro", "F", False),
    ("Skyeng", "t", False),
    ("Skyeng", "q", False)
])
@pytest.mark.negative
def test_contains_negative(input_string, symbol, expected):
    assert stringutils.contains(input_string, symbol) == expected
    # Негативные проверки
    assert stringutils.contains("Skypro", "F") is False
    assert stringutils.contains("Skypro", "t") is False
    assert stringutils.contains("Skypro", "q") is False


@pytest.mark.parametrize("input_string, symbol, expected", [
    ("Skypro", "p", "Skyro"),
    ("Skypro", "Sky", "pro"),
    ("Skypro", "yp", "Skro")
])
@pytest.mark.positive
def test_delete_symbol_positive(input_string, symbol, expected):
    assert stringutils.delete_symbol(input_string, symbol) == expected
    # Позитивные проверки
    assert stringutils.delete_symbol("Skypro", "p") == "Skyro"
    assert stringutils.delete_symbol("Skypro", "Sky") == "pro"
    assert stringutils.delete_symbol("Skypro", "yp") == "Skro"


@pytest.mark.parametrize("input_string, symbol, expected", [
    ("Skypro", "L", "Skypro"),
    ("Skypro", "!", "Skypro"),
    ("Skypro", "$", "Skypro")
])
@pytest.mark.negative
def test_delete_symbol_negative(input_string, symbol, expected):
    assert stringutils.delete_symbol(input_string, symbol) == expected
    # Негативные проверки
    assert stringutils.delete_symbol("Skypro", "L") == "Skypro"
    assert stringutils.delete_symbol("Skypro", "!") == "Skypro"
    assert stringutils.delete_symbol("Skypro", "$") == "Skypro"
