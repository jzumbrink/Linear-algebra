from set import Set


class Function:

    def __init__(self, domain: Set, codomain: Set, *behaviour):
        self.domain = domain
        self.codomain = codomain
        self.behaviour = [describing_rule for describing_rule in behaviour]

    def __call__(self, value):
        for describing_rule in self.behaviour:
            pot_result = describing_rule(value)
            if pot_result is not None:
                return pot_result
        return None

    # the following methods are just for finite domains and codomains
    def __eq__(self, other):
        if type(other) == type(self) and other.domain == self.domain and other.codomain == self.codomain:
            for x in other.domain:
                if other(x) != self(x):
                    return False
            return True
        return False

    def injective(self):
        pot_infinity_warning(self.domain)
        for x_1 in self.domain:
            for x_2 in self.domain:
                if x_1 != x_2 and self(x_1) == self(x_2):
                    return False
        return True

    def surjective(self):
        pot_infinity_warning(self.codomain)
        for y in self.codomain:
            for x in self.domain:
                if self(x) == y:
                    break
            else:
                return False
        return True

    def bijective(self):
        return self.injective() and self.surjective()


def pot_infinity_warning(s: Set) -> None:
    if not s.is_finite():
        print("This set is infinite. The following results may be just representive for the finite elements of the set.")


if __name__ == "__main__":

    f = Function(Set({1, 2, 23}), Set({1, 23}),
                 lambda x: 23 if x == 2 else None,
                 lambda x: x)
    print(f(1))
    print(f(2))
    print(f(3))
    print(f.injective())
    print(f.surjective())
    id_func = Function(Set({}), Set({}, 2), lambda x: x)
    print(id_func(323443))
