import random
import shutil
import os
from src.RandWord import RandWord
from src.HangMan import HANGMAN
from src.HangManLogo import HANGMANLOGO


def randword():
    return RandWord()


def HangMan(g):
    return HANGMAN(g)


def HangManLogo():
    return HANGMANLOGO()


def nl():
    print("")


def pycache_remove():
    pycache_path = "src/__pycache__"
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)


def spaced_word(w):
    space = " "
    spaced_word = ""
    word = w
    for i in word:
        spaced_word += i
        spaced_word += space
    return spaced_word


def underline(wl):
    char = "-"
    underline = char * wl
    return underline


def spaced_underline(ul):
    space = " "
    spaced_underline = ""
    for i in ul:
        spaced_underline += i
        spaced_underline += space
    return spaced_underline


def len_underline(w):
    word_len = len(w)
    return word_len


def get_one_letter(w):
    return random.choice(w)


def non_word(w, gl):
    new_none_word = ""
    none_word = "".join(ch if ch in gl else ' ' for ch in w)
    for i in none_word:
        new_none_word += i
        new_none_word += " "
    return new_none_word


def full_word(w, ul):
    return f"{w}\n{ul}"


def main_loop(g, la, gls, gl, w, wsul, wl, fw, sl):
    running = True
    while running:
        hangman = HangMan(g + 1)
        none_word = non_word(w, gl)
        print(none_word)
        print(wsul)
        nl()
        user_input = str(input(f"Your Guess({g}): "))

        if sl not in gl:
            gl.append(sl)

        if user_input:
            if len(user_input) < la:
                gls += user_input.strip()
                for char in gls:
                    if char not in gl and char.isalpha():
                        gl.append(char)
                if user_input == w or w in gl:
                    nl()
                    print(hangman)
                    print(fw)
                    print(f"You Win!({5 - g} chances used!)")
                    nl()
                    running = False

                elif g == 0:
                    print(HangMan(0))
                    print(fw)
                    print("You Lost!")
                    nl()
                    running = False

                elif g > 0 and user_input != w:
                    nl()
                    print(hangman)
                    print("Try again...")
                    nl()
            else:
                print(hangman)
                print(f"Too Many words at once, try {la}.")
                print("\n")

        elif g <= 0:
            print(HangMan(0))
            print(fw)
            print("You Lost!")
            running = False

        else:
            print(hangman)

        g -= 1


def main():
    # 7 tries
    guess = 6
    letters_allowed = 6
    guessed_letters_str = ""
    guessed_letters = []
    word = str(randword())
    word_spaced = spaced_word(word)
    word_len = len_underline(word)
    word_ul = underline(word_len)
    word_spaced_ul = spaced_underline(word_ul)
    fullword = full_word(word_spaced, word_spaced_ul)
    selected_letter = get_one_letter(word)
    hangman_logo = HangManLogo()

    try:
        print(word)
        nl()
        print(hangman_logo)
        main_loop(guess, letters_allowed, guessed_letters_str, guessed_letters, word, word_spaced_ul, word_len, fullword, selected_letter)
    except KeyboardInterrupt:
        print("\nExiting...")

    pycache_remove()


if __name__ == "__main__":
    main()
