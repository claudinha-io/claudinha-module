from claudinha_text.ascii_text import validate_args as validate

def test_show_text_with_no_user_message():
    message = validate(["program"])
    assert message == "Teste"

def test_show_text_with_user_message_and_no_color():
    message = validate(["program", "Olaar"])
    assert message == "Olaar"

def test_show_text_with_user_message_with_more_one_word_and_no_color():
    message = validate(["program", "1", "2", "3", "Teste"])
    assert message == "1 2 3 Teste"

def test_show_text_with_user_message_and_color():
    message = validate(["program", "blue", "Olaar"])
    assert message == ("Olaar", "blue")

def test_show_text_with_user_message_with_more_one_word_and_color():
    message = validate(["program", "red", "Olaar", "1", "2", "3", "Teste"])
    assert message == ("Olaar 1 2 3 Teste", "red")