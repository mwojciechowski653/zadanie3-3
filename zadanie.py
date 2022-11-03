def div(a,b):
  if b==0:
    return "Nie dzieli sie przez zero"
  else:
    return a/b
    
def test_answer():
  assert div(10,0)=="Nie dzieli sie przez zero"

def test_answer():
  assert div(10,5)==2
