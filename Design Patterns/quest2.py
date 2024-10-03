
class IValue:
    def operation(self, value):
        pass

class Value(IValue)     :
    def __init__(self, number=0):
        self.number = int(number)
        
    def operation(self, value):
        return self.number + value
    
    def __repr__(self):
        return str(self.number)
        
        
class Add(IValue):
    def __init__(self, value):
        self.value = value
    
    def operation(self, base_value):
        if isinstance(self.value, IValue):
            return base_value + self.value.operation(0)
        else:
            return base_value + self.value
        
        
class Sub(IValue):
    def __init__(self, value):
        self.value = value

    def operation(self, base_value):
        if isinstance(self.value, IValue):
            return base_value - self.value.operation(0)
        else:   
            return base_value - self.value
        
        
number = Value(10)
add = Add(10)
sub = Sub(5)

print("Original number: ", number)

add_result = add.operation(number.operation(0))
print("Add 10:", add_result)

sub_result = sub.operation(number.operation(0))
print("Sub 5:", sub_result)