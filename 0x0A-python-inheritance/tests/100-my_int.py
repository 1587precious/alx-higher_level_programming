class MyInt(int):
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)

# Example usage:
a = MyInt(5)
b = MyInt(7)

print(a == b)  # This will print False (inverted behavior)
print(a != b)  # This will print True (inverted behavior)

