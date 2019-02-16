from typing import List

from src.utilities import operators
from src.utilities import translations


class Translator:
    """class containing methods to translate bf sources into other 
    languages code
    """

    @staticmethod
    def bf_to_c(bf_sources: List[str]) -> List[str]:
        """translate brainfuck sources into c code

        :param bf_sources: 

        :return: the corresponding c sources
        """
        c_sources = [translations.CStyle.HEADER]
        [
            c_sources.append(translations.CStyle.TRANSLATIONS[op]) 
            for op in bf_sources
        ]
        c_sources.append(translations.CStyle.FOOTER)
        return c_sources


    @staticmethod
    def sanitize(sources: List[str]) -> List[str]:
        """delete all symbols that doesn't belong to the bf syntax

        :param sources: bf sources to sanitize
        
        :return: the sanitized bf instructions
        """
        return [
            op 
            for op in sources 
            if op in operators.BrainfuckOperator.get_operators()
        ]
