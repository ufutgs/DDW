import operator

def mergesort(arr, byfunc=None):
      if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergesort(L,byfunc)
  
        # Sorting the second half
        mergesort(R,byfunc)
  
        i = j = k = 0
        if byfunc != None:
          # Copy data to temp arrays L[] and R[]
          while i < len(L) and j < len(R):
              if byfunc(L[i]) < byfunc(R[j]):
                  arr[k] = L[i]
                  i += 1
              
              else:
                  arr[k] = R[j]
                  j += 1
              k += 1

          # Checking if any element was left
          while i < len(L):
              arr[k] = L[i]
              i += 1
              k += 1

          while j < len(R):
              arr[k] = R[j]
              j += 1
              k += 1
        else:
           # Copy data to temp arrays L[] and R[]
          while i < len(L) and j < len(R):
              if L[i]< R[j]:
                  arr[k] = L[i]
                  i += 1
              else:
                  arr[k] = R[j]
                  j += 1
              k += 1

          # Checking if any element was left
          while i < len(L):
              arr[k] = L[i]
              i += 1
              k += 1

          while j < len(R):
              arr[k] = R[j]
              j += 1
              k += 1

              
class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        pass

    def pop(self):
        return self.__items.pop() if len(self.__items)>0 else None
        pass

    def peek(self):
        return self.__items[len(self.__items)-1] if len(self.__items)>0 else None
        pass

    @property
    def is_empty(self):
        return True if self.peek() == None else False
        pass

    @property
    def size(self):
        return len(self.__items)
        pass
    
    def clear(self):
        self.__items = []


class EvaluateExpression:
  def __init__(self, string=""):
    self.valid_char = valid_char = '0123456789+-*/() '
    self.operrand = "0123456789"
    self.operator = "+-*/()"
    self.minus_op = "*/("
    self.array=[]
    self.yeet = None
    self.expression = string
    self.ops = {
                '+' : operator.add,
                '-' : operator.sub,
                '*' : operator.mul,
                '/' : operator.floordiv,  # use operator.div for Python 2
                '%' : operator.mod,
                '^' : operator.xor,
            }
    
    pass

  @property
  def expression(self):
    return self.yeet
    pass

  @expression.setter
  def expression(self, new_expr):
      for s in new_expr:
        if s not in self.valid_char:
          self.yeet = ""
          return
      self.yeet=new_expr
      self.insert_space()

  def insert_space(self) :
      self.array=[]
      self.yeet=self.yeet.replace(' ', '')
      state = "init"
      s = ""
      count = 0
      for i in self.yeet:
        if i in self.operrand:
          s+=i
        elif i =="-" and s=="" :
          s+=i
          if count>0:
            if self.array[-1] in ["+","-"]:
              self.array = None
              return
            else:
              if self.array[-1] not in self.minus_op:
                self.array.append("+")
          
        else :
          if (count ==0 and i in ["+","*","/",")"] ) or (i=="(" and s!=""):
              self.array = None 
              return
          if s!="":
            self.array.append(s)
            s=""
          self.array.append(i)
          if (self.array[-1] in ["+","*","/"] and self.array[-2] in ["+","*","/","("]):
            self.array = None
            return
        count+=1
      if s!="":
        self.array.append(s)
      print(self.array)

  def process_operator(self, operand_stack, operator_stack):
      try:
        if(operand_stack.size>1):
          a = operand_stack.pop()
          b = operand_stack.pop()
          operand_stack.push(self.ops[operator_stack.pop()](b,a))
        else:
          operator_stack.clear()
          operand_stack.clear()
      except Exception as e:
          print(str(e))
          operator_stack.clear()
          operand_stack.clear()

  def recursive(self,operand_stack,operator_stack):
    while operator_stack.size>0 and operator_stack.peek()!="(":
      self.process_operator(operand_stack,operator_stack)
      if operator_stack.peek() == ")":
        operator_stack.pop()
        self.recursive(operand_stack,operator_stack)
    if operator_stack.peek()=="(":
      operator_stack.pop()

  # phase 1 
  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    if self.array == None:
      return None
    for i in range(len(self.array)):
      a = self.array[i]
      if a in self.operator:
        if a == "*" or a =="/":
          if (operator_stack.peek()!="(") and (operator_stack.peek()=="*" or operator_stack.peek()=="/") and operand_stack.size>1:
            self.process_operator(operand_stack,operator_stack)
          operator_stack.push(self.array[i])
        elif a == "+" or a =="-":
          if (operator_stack.peek()!="(" and operand_stack.size>1):
            self.process_operator(operand_stack,operator_stack)
          operator_stack.push(a)
        elif a == ")":
          self.recursive(operand_stack,operator_stack) # call recursive to do braket first
      else:
        operand_stack.push(float(a))
    self.recursive(operand_stack,operator_stack)
    return int(operand_stack.peek()) if operand_stack.peek() != None else None
    
def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





