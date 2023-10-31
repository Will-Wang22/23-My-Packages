from numbers import Number, Integral

class Polynomial:
    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1
    
    # str(Polynomial), print(Polynomial)
    def __str__(self):
        Xs = [f"{c}x**{p}" for p, c in enumerate(self.coefficients)]
        return " + ".join(reversed(Xs))
    
    # repr(Polynomial)
    def __repr__(self):
        return f"{type(self).__name__}({self.coefficients!r})"
        # QUESTION: again, what does "!r" mean here? Representation?
    
    def __eq__(self, other):
        return type(self) is type(other) and self.coefficients == other.coefficients
        # Python will evaluate as many operands as it needs to in order to evaluate logical statement.
        # "is" returns whether the operands are the same object.

    # An example of encapsulation
    def __add__(self, other):
        if isinstance(other, type(self)):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients[:common], other.coefficients[:common]))
            coefs += self.coefficients[common: ] + other.coefficients[common: ]     # Note that this is well-defined as of the above must be empty.
            return Polynomial(coefs)
        # elif isinstance(other, Number):
        elif isinstance(other, Number):
            return self + type(self)((other,))
        else:
            return NotImplemented
            # If it returns NotImplemented, Python runs the right hand operator (__radd__ in this case).
            # It is almost equivalent to run "p + 1", "p.__add__(1)" and "Polynomial.__add__(p, 1)".
    def __radd__(self, other):
        return self + other