from um import count


def test_count_default():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_count_special():
    assert count(".um") == 1
    assert count("!um") == 1
    assert count("?um") == 1
    assert count(",um") == 1
    assert count("$um") == 1


def test_count_text():
    assert count("Hello, um, world") == 1
    assert count("This is, um... CS50") == 1
    assert count("Um... what are regular expressions?") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2
    assert (
        count(
            "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
        )
        == 2
    )


def test_count_limit():
    assert count(
        "um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um"
    ) == 248
