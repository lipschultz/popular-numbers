import itertools
import math
import sqlite3
from typing import Union, Optional


class NumberGenerator:
    def __init__(self,
                 real_min, real_max, real_decimal_places,
                 imag_min=None, imag_max=None, imag_decimal_places=None,
                 skip: Union[list, tuple, set, 'NumberGenerator'] = tuple(),
                 db_url: Optional[str] = None,
                 ):
        self.real_min = real_min
        self.real_max = real_max
        self.real_decimal_places = real_decimal_places
        self.db_url = db_url
        self.max_not_found_count = 100

        self.imag_min = imag_min if imag_min is not None else real_min
        self.imag_max = imag_max if imag_max is not None else real_max
        self.imag_decimal_places = imag_decimal_places if imag_decimal_places is not None else real_decimal_places

        self.skip = (skip,) if isinstance(skip, NumberGenerator) else skip

    @staticmethod
    def generate_numbers(min_val, max_val, decimal_places):
        fractional_resolution = 10 ** decimal_places
        outer_range = (
            whole + (frac / fractional_resolution)
            for whole in range(math.floor(min_val), math.ceil(max_val))
            for frac in range(fractional_resolution)
        )
        return (number
                for number in outer_range
                if min_val <= number < max_val
                )

    @staticmethod
    def _round_number(num, n_decimal_places):
        fmt = '{:0.' + str(n_decimal_places) + 'f}'
        return fmt.format(num)

    def _real_to_str(self, num):
        return self._round_number(num, self.real_decimal_places)

    _r2s = _real_to_str

    def _imag_to_str(self, num):
        return self._round_number(num, self.real_decimal_places)

    _i2s = _imag_to_str

    def get_generator(self):
        real_numbers = self.generate_numbers(self.real_min, self.real_max + 1, self.real_decimal_places)
        imag_numbers = self.generate_numbers(self.imag_min, self.imag_max + 1, self.imag_decimal_places)
        if self.db_url:
            def num_gen():
                db_conn = sqlite3.connect(self.db_url) if self.db_url else None
                not_found_count = 0
                for r, i in itertools.product(real_numbers, imag_numbers):
                    if any(complex(r, i) in skip for skip in self.skip):
                        continue
                    elif not_found_count < self.max_not_found_count and db_conn.execute(f"SELECT * FROM popularity WHERE real='{self._r2s(r)}' AND imag='{self._i2s(i)}' LIMIT 1").fetchone():
                        continue
                    else:
                        not_found_count += 1
                        yield complex(r, i)
                db_conn.close()
            return num_gen()
        else:
            return (complex(r, i)
                    for r, i in itertools.product(real_numbers, imag_numbers)
                    if not any(complex(r, i) in skip for skip in self.skip)
                    )

    def __iter__(self):
        return self.get_generator()

    def __len__(self):
        real_count = (self.real_max - self.real_min + 1) * 10**self.real_decimal_places

        imag_count = (self.imag_max - self.imag_min + 1) * 10**self.imag_decimal_places

        raw_count = int(real_count * imag_count)
        return raw_count  #  - sum(len(skip) for skip in self.skip)

    def __contains__(self, item):
        if isinstance(item, (list, tuple)):
            item = complex(item[0], item[1])

        if self.real_min <= item.real < self.real_max and self.imag_min <= item.imag < self.imag_max:
            # Subtract off the '0.' to get # decimal places
            real_dec = len(str(round(abs(item.real - int(item.real)), 10))) - 2
            imag_dec = len(str(round(abs(item.imag - int(item.imag)), 10))) - 2
            return (
                (self.real_decimal_places is not None and real_dec <= self.real_decimal_places) and
                (self.imag_decimal_places is not None and imag_dec <= self.imag_decimal_places)
            )

        return item in self.get_generator()