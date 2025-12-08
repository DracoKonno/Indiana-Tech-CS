'''
class Person:
    def __init__(self, name, age):
        self.name = name # Public
        self._age = age
    def get_age(self):
        return self._age if self._age > 0 else print("invalid age given")
# Test:
person = Person("Bob", 25)
print(person.get_age()) # Should print 25
# person._age = -5 # We shouldn't do this!
'''

# TODO: Store SSN privately, show only last 4 digits
class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.__ssn
    def get_masked_ssn(self):
        # Return like: ***-**-6789
        pass
    def verify_ssn(self, ssn_to_check):
        # Return True if matches stored SSN
        pass
