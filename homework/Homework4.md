## Homework 4



1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.

   [False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield]

2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다.
   (floating point rounding error)
   따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

   ```python
   a = 0.1 * 3
   b = 0.3
   round(a,1) == b
   ```

3. 1) \n

   2) \t

   3) \\\

4. name = "철수"

   ```python
   print(f"{name}야 안녕")
   
   
   
   ```

5. 5

       - int(float('3.5'))



# 여기에 코드를 작성하세요.
def tax(income):
​    if income <= 1200:
​        pay = income * 0.06
​    elif 1200 < income <4600:
​        pay = 1200 * 0.06 + (income-1200) * 0.15
​    else:
​        pay = 1200 * 0.06 + 3400 * 0.15 + (4600-income)*0.35
​    

    return pay