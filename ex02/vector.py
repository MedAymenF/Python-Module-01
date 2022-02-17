class Vector:
    def __init__(self, value):
        if isinstance(value, list):
            if not list(filter(lambda x: not isinstance(x, float), value)):
                self.values = value
                self.shape = (1, len(value))
            elif not list(filter(lambda x: not isinstance(x, list)
                                 or not len(x) == 1
                                 or not isinstance(x[0], float), value)):
                self.values = value
                self.shape = (len(value), 1)
            else:
                raise ValueError('Vector can only be initialized with \
a list of floats, a list of list of floats, a size, or a range.')
        elif isinstance(value, int):
            assert value > 0, "Size has to be greater than zero"
            self.values = list(map(lambda x: [float(x)], range(value)))
            self.shape = (value, 1)
        elif isinstance(value, tuple):
            assert len(value) == 2\
                    and isinstance(value[0], int)\
                    and isinstance(value[1], int), 'Not a proper range'
            assert range(*value), 'Range is empty'
            self.values = list(map(lambda x: [float(x)], range(*value)))
            self.shape = (len(self.values), 1)
        else:
            raise ValueError('Vector can only be initialized with \
a list of floats, a list of list of floats, a size, or a range.')

    def __str__(self):
        return f'Vector({self.values})'

    def __repr__(self):
        return f'Vector({self.values})'

    def T(self):
        if self.shape[0] == 1:
            values = list(map(lambda x: [x], self.values))
            return Vector(values)
        elif self.shape[1] == 1:
            values = list(map(lambda x: x[0], self.values))
            return Vector(values)

    def dot(self, vec):
        try:
            assert isinstance(vec, Vector), 'You can calculate \
a dot product only between two vectors of the same shape'
            assert self.shape == vec.shape, 'You can calculate \
a dot product only between two vectors of the same shape'
        except Exception as e:
            print(e)
        else:
            if (self.shape[0] == 1):
                return sum([x * y for (x, y) in zip(self.values, vec.values)])
            elif (self.shape[1] == 1):
                return self.T().dot(vec.T())

    def __add__(self, vec):
        try:
            assert isinstance(vec, Vector),\
                'You can only add a vector of the same shape'
            assert self.shape == vec.shape,\
                'You can only add a vector of the same shape'
        except Exception as e:
            print(e)
        else:
            if (self.shape[0] == 1):
                result = [x + y for (x, y) in zip(self.values, vec.values)]
            elif (self.shape[1] == 1):
                result = [[x[0] + y[0]]
                          for (x, y) in zip(self.values, vec.values)]
            return Vector(result)

    def __radd__(self, vec):
        pass

    def __sub__(self, vec):
        try:
            assert isinstance(vec, Vector),\
                'You can only substract a vector of the same shape'
            assert self.shape == vec.shape,\
                'You can only substract a vector of the same shape'
        except Exception as e:
            print(e)
        else:
            if (self.shape[0] == 1):
                result = [x - y for (x, y) in zip(self.values, vec.values)]
            elif (self.shape[1] == 1):
                result = [[x[0] - y[0]]
                          for (x, y) in zip(self.values, vec.values)]
            return Vector(result)

    def __rsub__(self, vec):
        pass

    def __mul__(self, scalar):
        try:
            assert isinstance(scalar, (int, float)),\
                'You can only multiply a vector by a scalar'
        except Exception as e:
            print(e)
        else:
            if (self.shape[0] == 1):
                result = [x * scalar for x in self.values]
            elif (self.shape[1] == 1):
                result = [[x[0] * scalar]
                          for x in self.values]
            return Vector(result)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        try:
            assert isinstance(scalar, (int, float)),\
                'You can only divide a vector by a scalar'
            assert scalar, "Can't divide by zero"
        except Exception as e:
            print(e)
        else:
            if (self.shape[0] == 1):
                result = [x / scalar for x in self.values]
            elif (self.shape[1] == 1):
                result = [[x[0] / scalar]
                          for x in self.values]
            return Vector(result)

    def __rtruediv__(self, scalar):
        print("Can't divide by a vector")
