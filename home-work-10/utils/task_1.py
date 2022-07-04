def write_to_file(name, phrase):
    if not isinstance(name, str):
        raise TypeError(TypeError)
    if not isinstance(phrase, str):
        raise TypeError(TypeError)
    f = open(name, 'w')
    f.write(phrase)
    f.close()
