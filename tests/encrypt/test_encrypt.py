import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Test with odd key
    assert encrypt_message("HelloWorld!", 3) == "leH_!dlroWol"
    assert encrypt_message("This is a test", 7) == "si sihT_tset a "
    assert encrypt_message("Trybe", 3) == "yrT_eb"

    # Test with even key
    assert encrypt_message("Hello, world!", 4) == "!dlrow ,o_lleH"
    assert encrypt_message("This is a test", 6) == "tset a s_i sihT"
    assert encrypt_message("Trybe", 2) == "eby_rT"

    # Test with invalid key
    assert encrypt_message("Hello, world!", -1) == "!dlrow ,olleH"
    assert encrypt_message("This is a test", 20) == "tset a si sihT"

    # Test with invalid message type
    with pytest.raises(TypeError):
        encrypt_message(12345, 5)

    # Test with invalid key type
    with pytest.raises(TypeError):
        encrypt_message("Hello, world!", "key")
