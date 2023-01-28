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

    def injective(self) -> bool:
        pot_infinity_warning(self.domain)
        for x_1 in self.domain:
            for x_2 in self.domain:
                if x_1 != x_2 and self(x_1) == self(x_2):
                    return False
        return True

    def surjective(self) -> bool:
        pot_infinity_warning(self.codomain)
        for y in self.codomain:
            for x in self.domain:
                if self(x) == y:
                    break
            else:
                return False
        return True

    def bijective(self) -> bool:
        return self.injective() and self.surjective()

    def inverse_function(self):
        inverse_map = {}
        if self.bijective():
            for x in self.domain:
                for y in self.codomain:
                    if self(x) == y:
                        inverse_map[y] = x

            return Function(self.codomain, self.domain, lambda y: inverse_map[y])
        else:
            raise RuntimeError


def pot_infinity_warning(*sets: Set) -> None:
    for s in sets:
        if not s.is_finite():
            print(
                "This set is infinite. The following results may be just representive for the finite elements of the set.")
            break


if __name__ == "__main__":
    f = Function(Set({1, 2, 23}), Set({1, 23}),
                 lambda x: 23 if x == 2 else None,
                 lambda x: x)
    print(f(1))
    print(f(2))
    print(f(3))
    print(f.injective())
    print(f.surjective())
    print(f.bijective())
    id_func = Function(Set({}), Set({}, 2), lambda x: x)
    print(id_func(323443))

    g = Function(
        Set({i for i in range(10)}),
        Set({i for i in range(10)}),
        lambda x: 2 if x == 3 else None,
        lambda x: 0 if x == 9 else None,
        lambda x: 1 if x == 0 else None,
        lambda x: 3 if x == 1 else None,
        lambda x: 9 if x == 2 else None,
        lambda x: x if 4 <= x <= 8 else None
    )

    print(g.bijective())
    print("\n===g(x)===")
    for i in range(10):
        print("g({}) = {}".format(i, g(i)))

    print("\n===g^-1(y)===")
    for i in range(10):
        print("g^-1({}) = {}".format(i, g.inverse_function()(i)))
