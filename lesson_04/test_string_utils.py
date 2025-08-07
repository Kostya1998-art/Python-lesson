from string_utils import StringUtils

stringutils = StringUtils()


def test_capitalize():
    # Позитивные проверки
    assert stringutils.capitalize("skypro") == "Skypro"
    assert stringutils.capitalize("hello world") == "Hello world"
    assert stringutils.capitalize("535")

    # Негативные проверки
    assert stringutils.capitalize("") == ""
    assert stringutils.capitalize(" ") == " "
    assert stringutils.capitalize("1234my") == "1234my"


def test_trim():
    # Позитивные проверки
    assert stringutils.trim(" skypro") == "skypro"

    # Негативные проверки
    assert stringutils.trim("sky pro") == "sky pro"
    assert stringutils.trim("...skypro") == "...skypro"
    assert stringutils.trim("skypro  ") == "skypro  "
    assert stringutils.trim("skypr o") == "skypr o"
    assert stringutils.trim("skyp  ro") == "skyp  ro"


def test_contains():
    # Позитивные проверки
    assert stringutils.contains("Skypro", "S") is True
    assert stringutils.contains("Skyeng", "g") is True
    assert stringutils.contains("Skyeng", "n") is True

    # Негативные проверки
    assert stringutils.contains("Skypro", "F") is False
    assert stringutils.contains("Skypro", "t") is False
    assert stringutils.contains("Skypro", "q") is False


def test_delete_symbol():

    # Позитивные проверки
    assert stringutils.delete_symbol("Skypro", "p") == "Skyro"
    assert stringutils.delete_symbol("Skypro", "Sky") == "pro"
    assert stringutils.delete_symbol("Skypro", "yp") == "Skro"

    # Негативные проверки
    assert stringutils.delete_symbol("Skypro", "L") == "Skypro"
    assert stringutils.delete_symbol("Skypro", "!") == "Skypro"
    assert stringutils.delete_symbol("Skypro", "$") == "Skypro"
