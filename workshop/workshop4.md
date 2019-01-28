## Workshop 4

v 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로
의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

```pytho
n = 5
m = 9
a = "*"*n
b = f"{a}\n"*m
print(b)
```



v 다음 딕셔너리에서 평균 점수를 출력하시오.



```python
student = {'python':80, 'algorithm' :78, 'django':95, 'flask':80}
print(sum(student.values())/len(student))

    
```



v 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형
별 학생수의 합계를 구하시오.



```python
blood = ['A','B','O','A','B','A','AB','AB','O','A','O','AB','O']
blood_dict = {}
for b in blood:
    if b in blood_dict:
        blood_dict[b] += 1
    else:
        blood_dict[b] = 1
print(blood_dict)
    
```

