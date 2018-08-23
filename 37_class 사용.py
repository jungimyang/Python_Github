'''
list에 replace 메서드를 추가한 AdvancedList 클래스를 작성.
x.replace(1,100) 메서드를 호출하여 -> 리스트의 1의 값을 100으로 변경하여 출력
[100, 2, 3, 100, 2, 3, 100, 2, 3]

(설명)
list에 replace 메서드를 추가하라고 했으므로 list 클래스를 상속받아서 AdvanceList를 만듭니다.
따라서 class AdvancedList(list):와 같이 만듭니다.

replace 메서드는 리스트에서 특정 값으로 된 요소를 찾아서 다른 값으로 바꾼다고 했습니다.
먼저 클래스의 메서드 안에서 현재 객체를 조작하려면 self를 이용해야 합니다.
여기서는 AdvancedList는 list를 상속받았으므로 self는 리스트(list)입니다.
그러므로 리스트의 모든 메서드를 사용할 수 있습니다.

특정 값을 찾을 때는 리스트의 index 메서드를 사용하고,
index로 찾은 인덱스를 self에 지정해준 뒤 새 값을 할당하면 값을 바꿀 수 있습니다.
이때 리스트에서 같은 값이 여러 개 들어있을 수도 있으므로 모든 값을 바꿔주어야 합니다.
따라서 while로 self에 특정 요소가 있을 때 계속 반복하도록 만든 뒤 요소를 바꿔주면 됩니다.
특정 요소가 있는지 확인할 때는 in 연산자를 사용하거나 self.count(찾을값)처럼 count 메서드를 사용해도 됩니다.


'''

class AdvancedList(list):
    def replace(self,old,new):
        while old in self:
            self[self.index(old)] = new

x = AdvancedList([1,2,3,1,2,3,1,2,3])
x.replace(1,100)
print(x)


