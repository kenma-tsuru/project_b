def count_vowel(text):
    n_a = text.lower().count("a")
    n_e = text.lower().count("e")
    n_i = text.lower().count("i")
    n_o = text.lower().count("o")
    n_u = text.lower().count("u")
    return n_a + n_e + n_i + n_o + n_u