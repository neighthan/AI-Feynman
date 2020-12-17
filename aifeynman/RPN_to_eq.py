# Turns an RPN expression to normal mathematical notation

_VARIABLES = {
    "0": "0",
    "1": "1",
    "P": "pi",
    "a": "x0",
    "b": "x1",
    "c": "x2",
    "d": "x3",
    "e": "x4",
    "f": "x5",
    "g": "x6",
    "h": "x7",
    "i": "x8",
    "j": "x9",
    "k": "x10",
    "l": "x11",
    "m": "x12",
    "n": "x13",
}
_OPS_UNARY = {
    ">": "({}+1)",
    "<": "({}-1)",
    "~": "(-{})",
    "\\": "({})**(-1)",
    "L": "log({})",
    "E": "exp({})",
    "S": "sin({})",
    "C": "cos({})",
    "A": "abs({})",
    "N": "asin({})",
    "T": "atan({})",
    "R": "sqrt({})",
    "O": "(2*({}))",
    "J": "(2*({})+1)",
}
_OPS_BINARY = set("+*-/")


def RPN_to_eq(expr: str) -> str:
    stack = []

    for i in expr:
        if i in _VARIABLES:
            stack.append(_VARIABLES[i])
        elif i in _OPS_BINARY:
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(f"({a2}{i}{a1})")
        elif i in _OPS_UNARY:
            a = stack.pop()
            stack.append(_OPS_UNARY[i].format(a))
    return stack[0]
