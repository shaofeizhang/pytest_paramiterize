import functions
import pytest
import parameters

lineList = [line.rstrip('\n') for line in open("input.txt")] 
processedList = []
for line in lineList:
    res = tuple(map(int, line.split(','))) 
    processedList.append(res)
    
    
inputs = parameters.Inputs()
input_suite1 = inputs.input_suite1
input_suite2 = inputs.input_suite2
    
@pytest.mark.parametrize('input1,input2,input3,input4,input5,result1,result2',
                         processedList)
def test_suites(input1,input2,input3,input4,input5,result1,result2):
    assert functions.test1(input1,input2) == result1
    assert type(functions.test2(input3)) is int
    assert functions.test3(input4,input5) == result2
    
######################################################################################################

inputs = parameters.Inputs()
input_suite1 = inputs.input_suite1
input_suite2 = inputs.input_suite2
input_suite3 = inputs.input_suite3

@pytest.mark.parametrize('input1,input2,result',
                         input_suite1)
def test_suite1(input1,input2,result):
    assert functions.test1(input1,input2) == result

    
@pytest.mark.parametrize('input1,input2,input3,result',
                         input_suite2)
def test_suite2(input1,input2,input3,result):
    assert functions.add3String(input1,input2,input3) == result
