from typing import List


class BrainfuckOperator:
    """Class to list all the operators
    """
    # moves
    ptr_next = '>'
    ptr_prev = '<'
    # operations
    ptr_decr = '-'
    ptr_incr = '+'
    # loop ctrl
    loop_beg = '['
    loop_end = ']'
    # io
    cell_inp = ','
    cell_show = '.'

    @classmethod
    def get_operators(cls) -> List[str]:
        """return all bf operators
        """
        return [
            cls.ptr_next,
            cls.ptr_prev,
            cls.ptr_decr,
            cls.ptr_incr,
            cls.loop_beg,
            cls.loop_end,
            cls.cell_inp,
            cls.cell_show
        ]
