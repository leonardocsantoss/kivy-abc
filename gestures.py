#!/usr/bin/env python
from kivy.gesture import GestureDatabase

gdb = GestureDatabase()

gestures = {
    'a': gdb.str_to_gesture('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'),
    'e': gdb.str_to_gesture('eNq1WN1OKzcQvt8XgZsiz5/HfgF6W4kHqChEgM4pRJDT9rx9xzPOrkOWLlIFF1ky+fx5PN/8OLl8+vb018+rh93b4cfrbvq1P/dpurzfw3Rz8Xz75+5i2qP9aw+a3m4u3g6vL992b/aWp8vve5kuV0luHDbtc6NSW79/eXo+tGWlLasfLPutoaY9hAfNhZ+2BHC6/iVdSVJgLNJfpbnzT/uY4mNGJqiKWiqA5Ontj9v/3oV9F5ke+gZcU4FMmIVSBmSd3h46OVOmVAWpxOs2uZ8cdCEXHtkHbgKtjKC5aFIuuM1dnLvO3OaV+YvMpWqVKrSQQwVu0eCMUiTRJjl67BG+hhydnBZybpxQKCtxrnXgFs5zSGrF7ZCj64mLnpgXt6Fw4oXdpMDO7DnD2+wuKC6CAg25ghaCzm7kqUgpTELKwDVn2GZ3SbF+DTu5prRomk4iQyXLQk8KUkumyiJaSLbZXVTqohoDNimpqIpAsrzWhVypBC8SYCXdJndRSWbyMnBjGsJS7RxLVLRuU7uipEdqKEu8LTalzNwmRuq8LTSynejkelI9cmOZXW5tgGnhzpRrYs3gr7pd/uxqMhy5CccSIv0/1C4lz1LyaXkOXisUWULyiabFLiTPQnIeejkwL9SY65whKGm7NNmFZN2kTmxd/aiiJfhnuF1InoUkHZix0NhTJOvSxatl0ya7uJQySDlOOJshQ8MyZZeOJduVI66lzFqiRO4d28rgOaSqfWq2Vq7bHUVcTZnVhHdhKQM5WH9JwjHivMdvkbueokvNjxOo1HECvZudnwi5CypLp7XGUYcsL4PrKZfaRxsnIN7O8uyCZvgidpc0L+MTTlotppH99MaSt+dndk3zMj+hjtzWcOY6Qq5DGQltN8TsmuZlfOJJxhjd0MkTIqTjjPvEbM6uaR4vRKthsV2tu2iyyCdU22M7F9UFVfgKaldTabgijtdPzDO1vZe5jUPdjra6lLpIKQDjxF+8ptMZgc7d7vl3r7vd83xr19yu7arT5bWd8ipN13Z0exz2WqZbM2oKY7X7yfBHDVEdUckRgOeIkhqCkgQiO3EBNyK6EdNVHf+0IdAREsRUYxm5MccyzivL2BHdY8EVhDiiBCLHQUtuRqvUUzxP5ngKhAaiOXJtt/owenwYihupc3lILLXd6Ac47KtHgck9J9XTOOWG8JAwp/cf2aadAz9EQEdQIHwXK78w8mj0hxkljBBGDmNEgfL5BiyBiCgQx7JujChQOgsec145aI8Preyi7ykO9n0xDUH+AAJHcT7lgdV24D0HuOtm10DPjJrDKt0aGVXCaqqubB8ppeEhwNqOOSBeXpyO3BpWT3JrtmsLS0AicUrqC+to1SgqgCg1dVEpywodwAgR7AtxtHZZbbafWPvW0OMRPvdGYbeLiF1gE65t3WtMzkTCsnZyiFzrPSLTSuAhMg9rVDt3XyLB5LyYkfS8IdiXxcAHC+EaJBJM5divztqctWCHlHK+a8prlFGrvXMmWqOMyj3Pi4/wJkJ0+Mfd08PjwX9eaWh+l7XQfl75++n+8OgQbWc6a0kGObx8373ePt/tHFb8MtjsfTD9vn99uf9xF/tUy+sru2PWwjaGqiabozZvrv4FaZqffg=='),
    'i': gdb.str_to_gesture('eNq1l91OJEcMhe/7ReAmqPxvv8DsbSQeICIwArQbGMFskn37uFxDT48C6VXQzE3DaddXZZ8qd/fl49fHP39c3W9f999fttOXw3XXpsu7HUzXF083f2wvph3mn3mh6fX64nX/8vx1+5r/8nT5bSfT5buQ6wqbdtpRluN3z49P+z7M+7D4YNivPWrawVhBX8KPHAI4bX5pV+DRWBlNzIXMaj1/9/tU99FV0YyFmIgB8/7vN/89D9c8Mt33KXKGloNBhJuhk3MS7g9wIEEBCc+7JI1wHV65g50H7gWPs8Cxyo9wHjgWnGa4WaA2DnZRR7YFHIGjATVVZsa2biiWoSjngZehOBuKrEZE7pFFQIoju5kouBg0AgYWXWeXnzj7SblWkMYJALImsoALZioWI4HmuE6nMpRmQxmUxdM2yeOCsqhKG2cnE1NQj5x5HV6G0mwoU0OIPImH8izgGMbWMqPIbaRu6+zyk+Qn2OSBQEhZuQgUXmeXnTTbSX2HSCKaMGfqvIAv3JSW0/9EyctQOhralHKnvRVel4YeyQ4Atr4Tufzk2c9kL/fL0lDIPgg5pRuZk4qvw8tPpvPAy1CW88DLUT44WhvOObLY7orBQOqf6VxclnKcCS9lqsCMh4Jya3n8tUHfdJ+gl6tCMx1z9c08hNWZteGn6GWryJEuhKoK0JTNFD/Td6VslaOtp+hGy/6VzdjbWzNAX29fUq7K0dWsuYM1DfNE46LqrVfDOR8p7hhZofUmo2WqwpnoZaoeTeVQcnEzgHDEt7JXB4tQSMPVVNP4dXZZqnIWdjmqR0fzdU5t3pA2o8EBFSGPV+5Jip/oAVp2apwBbeWlwSqaG3A+9DlAMJv7ej2sfDQ6A7lcNPlf5P66f/uy3T7NL+/Zg/Lt3Wy63GDgVZs2+bjKy35nPt38W4wuEkoXkaxEb0P0EgWvYvmzHgEVQSNCfQzDEplKdBkiDbGTN9QOIg/Rh3gYLksReIg6xDgR7UTM+ZY/7RF+wnovIk7WFQWOkTjrcl0BJ+LIIA65jrrFYfghVxgiDnHkSjGqAkMcuVIrEQ8T6dKLt9ltIYLraSbUI3wZYW0Mi4WF+aAoEdrIj0Yov2MsNFgkBsiHgSNdGXsn6/nOwJG8jhmzTCchUSGjFNGhm9D3IFWX/Ir5OKKKlI+ljyNsRMTHEVUxFvg4Ik4jTooOPSI/gG/GAXzYPt4/7PtHbn4ObxB6AVL+6/Fu/1AqvjmQ6v752/bl5ul2W3dGm+v6oTf8tnt5vvt+O2g8bTh7uoFzPnl6K4zeAq/+Ab4mHLE='),
    'o': gdb.str_to_gesture('eNq1WNtuHDcMfd8fiV9qiBeR0g+4rwXyAYWTLBwjqb2wN23z99WQnJEmnvXsSz0ANzmmzlA8JKX1zeO3x79/3j4cX88/Xo6H3+PzlA43X05w+Pjh6f6v44fDCds/2wcdXj9+eD2/PH87vrb/8uHm+ykfbjZJPprb4SQTlbb1p+fHp/O0rEzL6oVlf0xehxN4BFMIP9sSwMNdukXKWoRnyxbOv9Ov6XD3W7pNqAy6WOLD66f791/D9pp8eIg3JIDMHDZJY3gIckCphQe7T25bB53JARJyJrepFujkmLgm6Zb2yYuR15k85YJVMayWPJAzFdFud7nRko/g3FNiCQWghCXGkb0oZO1W9+nR6GmhB6jjk7GzEyhL6nZfUjRJMS/smLIqprCCOrATq8piyxXspinqwt6EFCngtkk7kCNoqd1eQW6aYu3kK4KaZUj7uhp1P+1kqlJXlalmKui21fxQ61WQy2Kb/y65aUpdU844PDTkJWlOJN3CPrlJSl1STqOmsJTjNAJWD9EVoZukNEoK4yML+di/zeYrcm6KUlcUV9SpdG5eP/vVwqYndz1hNZ544M5F26ZmW/anC5ucTPsTwLYkWha7P17Y5OQuZ0pIqZTZapom+8KeU9LF7hcLm5y8TN1UcXxwYK5E0u0VgZuavMxc0AwlUViWXimYhLguNu9SZxMzw3IQ8eon9bCBULMstlzBbWJm2ude9hI2yT65iZmvOUETsxIN9gp2EzP3IxRpeMZRPtRPs21i7nObmrmfoLQiT3UkJ6nc7S63mJwynKDrkdoCHNhTa3dabLve7Fe5mKZyVYOmkoG02/1CFxNVhg5d7V+5DkOxrKom7w9cMVGld+h6gIB2coJS2xAPu6+pmKZSd5t/3QIs++NWTVKF/4PaxNSlQWF1zVVdqDOtnv3WVxNSe3fy0J7t4F+YhSo2VWdrMU93/c8vx+PTcnNvyrSrewvo5o6w3qbDHSO3j/Op1fP9W7A6WEawJAfBQXQQDAQ1EMptHX948kD3oMseZB5J3EOcmCcQq4cA8bbsoHum6qA46C+YWMYfmTzUPIpxteT5suIgO5g24qruYcQ0rf6VuFpKUKt7kBFXcNCJFd8SV0tJO+vNQ2DDg9wjmwerE3tKBB3EjXg8P5LMgzxp1fOTffeYN5bpyiOWlREET1qtK9ALA1Ia0URv99OGg0dmxeOqTigOO3JZJzQ2b3Su2oT67pUcxUB9x2oV4UJMqAy6+C8nNMrAatWzP6G+z5ocnd/mG63saDBAGoqyo94DKRhyoFH3v6Be61DWKA+t1VHbWztyfRcpUNsbcaAaqDrqeytzZN7c2QstzQze3RJyb1Q+oPe6eqmhbLn4rqP22Wsf0HcdXbVV2u0m4C5e27MM6CmwyNtHhIp5ROtmqLJyCf1QB5TTHF0ZXs1Jt+g8OSXGVcRBng+ruoZuVThFPi5Pwnbpcxd5x8WTY2IvkxfIkyO+EENd8uQIrVEZNO+o5yMHQ1QNRX2kNeopYF4xsKeAgpfejpH27cdd5B0XTwHFIQLBTUOld5THo2kzXewpwDweHcAynlRxdgB7CjCtlOUyNORUEo7W8VjbOlPa9xp3iVqKmDMM6FKNGVcob9HFYIjjKGLOPKJbRxDkvHLhjSxlGV9f5lB1RHUrvTmS4701lfbb10emfAxojC6Ju4IfnQobCwUG6WiebuKZQlmjY33QPHfFk0MxSPLWS2KE+qiTaCeJEerTTWI4SLQIXB5dEv2S33FZDVeJXGsahkNHPQUF1qinwO8zS3RqKfA7TwzmCbUUsFcvzQed2q45dr05NdVSwJnn6t1wUXepl3vAL4+scHks+lWSY57iVnn6xZL9XL7gAu7ypkibf/TYdM/0u+/X4+PD1/P01+V2s7wDy2CD/3n8cv5qaFvWvmv+StVczs/fjy/3T5+P5pbtSj/hcUf/8/Ty/OXHZ6eWltrbXBlrbt8iJCfU6Wvtp9v/AFOnskU='),
    'u': gdb.str_to_gesture('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'),
}