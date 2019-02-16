from typing import List

from src.translator import Translator


DEFAULT_BF_SOURCES = 'etc/hello_world.bf'


def read_sources(filename: str) -> List[str]:
    """read char by char a source file

    :param filename: path to the source file

    :return: its content as a list of char
    """
    bf_sources: List[str] = []

    with open(filename, 'r') as source:
        for line in source:
            [bf_sources.append(char) for char in line]

    return bf_sources


if __name__ == '__main__':
    sources = read_sources(DEFAULT_BF_SOURCES)
    sources = Translator.sanitize(sources)
    c_sources = Translator.bf_to_c(sources)
    print(''.join(c_sources))
