from src.utilities.operators import BrainfuckOperator as bf


class CStyle:
    """class containing translations to convert bf to c
    """

    HEADER = '#include <stdio.h>\n' \
        + 'int main(int argc, char **argv) {' \
        + 'int tab[256] = {}; int *ptr = &tab[0];'

    FOOTER = 'ptr = NULL; return 0;}'

    TRANSLATIONS = {
        # moves
        bf.ptr_next: '++ptr;',
        bf.ptr_prev: '--ptr;',
        # operations
        bf.ptr_decr: '--(*ptr);',
        bf.ptr_incr: '++(*ptr);',
        # loop ctrl
        bf.loop_beg: 'while(*ptr != 0) {',
        bf.loop_end: '}',
        # io
        bf.cell_inp: '*ptr = getchar();',
        bf.cell_show: 'printf("%c", *ptr);',
    }
