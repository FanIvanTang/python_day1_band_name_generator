from main import band_name_generator
from tud_test_base import set_keyboard_input, get_display_output


def test_case_1():

    set_keyboard_input(["Shenzhen", "Dodo"])

    band_name_generator()

    output = get_display_output()

    assert output == [
        "Welcome to the Band Name Generator.",
        "What's name of the city you grew up in?\n",
        "What's your pet's name?\n",
        "Your band name could be Shenzhen Dodo\n",
    ]


def test_case_2():

    set_keyboard_input(["Chengdu", "Ahuang"])

    band_name_generator()

    output = get_display_output()

    assert output == [
        "Welcome to the Band Name Generator.",
        "What's name of the city you grew up in?\n",
        "What's your pet's name?\n",
        "Your band name could be Chengdu Ahuang\n",
    ]
