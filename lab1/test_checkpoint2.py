from checkpoint2 import substract, divide
def test_substract():
    assert substract(5,2)==3
    assert substract(1,-1)==2
def test_divide():
    assert divide(6,2)==3
    assert divide(1,0)==None
