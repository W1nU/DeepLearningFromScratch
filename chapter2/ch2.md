## 퍼셉트론

### 퍼셉트론이란?

퍼셉트론은 다수의 신호를 입력으로 받아 하나의 신호를 출력합니다. 여기서 말하는 신호란 전류나 강물처럼 흐름이 있는 것을 상상하면 좋습니다. 전류가 전선을 타고 흐르는 전자를 내보내듯, 퍼셉트론 신호도 흐름을 만들고 정보를 앞으로 전달합니다. 

다만 실제 전류와 달리 퍼셉트론 신호는 흐은다/안 흐른다(1 이나 0)의 두 가지 값을 가질 수 있습니다. 이 글에서는 1을 신호가 흐른다, 0을 신호가 흐르지 않는다는 의미로 사용합니다

![image-20200624223500008](/Users/seungwoojung/Library/Application Support/typora-user-images/image-20200624223500008.png)

이 그림은 입력으로 2개의 신호를 받는 퍼셉트론의 예입니다. x1과 x2는 입력 신호, y는 출력 신호, w1과 w2는 가중치를 의미합니다. 그림의 원을 뉴런 혹은 노드라고 부릅니다. 입력 신호가 뉴런에 보내질 때는 각각 고유한 가중치가 곱해집니다.

이 떼 뉴런에서 보내온 신호의 신호의 총합이 정해진 한계를 넘어설 떄문 1을 출력하고 이를 뉴런이 활성화한다 라고 표현합니다. 이 글에서는 그 한계를 임계값이라 하며, θ 기호로 나타냅니다.

이를 수식으로 나타내면 아래 식이 됩니다. 

![image-20200624223748837](/Users/seungwoojung/Library/Application Support/typora-user-images/image-20200624223748837.png)

퍼셉트론은 복수의 입력 신호 각각에 고유한 가중치를 부여합니다. 가중치는 각 신호가 결과에 주는 영향력을 조절하는 요소로 작용합니다. 즉, 가중치가 클수록 해당 신호가 그만큼 더 중요함을 뜻합니다. 



### 퍼셉트론 구현하기

#### 간단한 구현

이제 논리 회로를 파이썬으로 구현해봅시다, 다음은 x1과 x2를 인수로 받는 AND라는 함수입니다.

```python
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7

    temp = x1 * w1 + x2 * w2

    if temp <= theta:
        return 0
    
    elif temp > theta:
        return 1

print(AND(0, 0)) # 0
print(AND(0, 1)) # 0
print(AND(1, 0)) # 0
print(AND(1, 1)) # 1
```

매개변수 w1, w2, theta는 함수 안에서 초기화하고, 가중치를 곱한 입력의 총합이 임계값을 넘으면 1을 반환하고 그 외에는 0을 반환합니다. 



#### 가중치와 편향 도입

앞에서 구현한 AND 게이트는 직관적이고 알기 쉽지만, 앞으로를 생각해서 다른 방식으로 수정하고자 합니다. 그 전에 θ를 -b로 치환하면 퍼셉트론의 동작이 아래 식처럼 됩니다.

![image-20200624225720133](/Users/seungwoojung/Library/Application Support/typora-user-images/image-20200624225720133.png)

본 글에서 소개한 식 두개는 기호 표기만 바뀌었을 뿐, 그 의미는 같습니다. 여기에서 b를 편항이라 하며 w1과 w2는 가중치 입니다. 위의 식 관점에서 해석해보자면, 퍼셉트론은 입력 신호에 가중치를 곱한 값과 편향을 합하여, 그 값이 0을 넘으면 1을 출력하고 그렇지 않으면 0을 출렵합니다. 그럼 넘파이를 이용하여 위의 식을 구현해보겠습니다.

```python
import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

print(w * x) # array([ 0. , 0.5])
print(np.sum(w * x)) # 0.5
print(np.sum(w * x) + b) # -0.19999999999999996 대략 -0.2（부동소수점 수에 의한 연산 오차）
```



#### 가중치와 편향 구현하기

가중치와 편향을 도입한 AND 게이트는 다믕과 같이 구현할 수 있습니다. 

```python
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    temp = np.sum(x * w ) + b

    if temp <= 0:
        return 0

    else:
        return 1
```

가중치는 입력 신호가 결과에 주는 영향력(중요도)을  조절하는 매개변수고, 편향은 뉴런이 얼마나 쉽게 활성화되는지를 조정하는데 사용됩니다. 

이어서 NAND 게이트와 OR 게이트를 구현해봅시다.

```python
import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # AND와는 가중치 w와 b만 다르다
    b = 0.7

    temp = np.sum(w * x) + b

    if temp <= 0:
        return 0
    
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # AND와는 가중치 w와 b만 다르다
    b = -0.2

    temp = np.sum(x * w) + b

    if temp <= 0:
        return 0
    
    else:
        return 1
```

앞 절에서 AND, NANA, OR는 모두 같은 구조의 퍼셉트론이고, 차이는 가중치 매개변수의 값 뿐이라 했습니다. 실제로 파이썬으로 작성한 NAND와 OR 게이트 코드에서도 AND와 다른 곳은 가중치와 편향 값을 설정하는 부분뿐입니다.



### 퍼셉트론의 한계

지금까지 살펴본 것처럼 퍼셉트론을 이용하면 AND, NAND, OR의 3가지 논리 회로르 ㄹ구현할 수 있었습니다. 다만 XOR 게이트는 구현할 수 없습니다. 또한 퍼셉트론은 직선 하나로 나눈 영역만 표현할 수 있다는 한계가 있습니다. 



#### 다층 퍼셉트론의 충돌

안타깝게도 퍼셉트론으로는 XOR 게이트를 표현할 수 없었습니다. 이를 보완하기 위해 퍼셉트론의 층을 쌓아 다층 퍼셉트론을 만들 수 있습니다. 이번 절에서는 층을 하나 더 쌓아서 XOR을 표현할 수 있습니다.

XOR 게이트는 AND, NAND, OR을 조합하여 만들 수 있습니다.

![image-20200624232104624](/Users/seungwoojung/Library/Application Support/typora-user-images/image-20200624232104624.png)





#### XOR 게이트 구현하기

이어서 위에서 조합된 XOR 게이트를 파이썬으로 구현해보겠습니다. 

```python
import AND
import NAND_OR
 
def XOR(x1, x2):
    s1 = NAND_OR.NAND(x1, x2)
    s2 = NAND_OR.OR(x1, x2)
    y = AND.AND(s1, s2)

    return y

print(XOR(0,0)) # 0
print(XOR(1,0)) # 1
print(XOR(0,1)) # 1
print(XOR(1,1)) # 0
```

