# 15650. 10828,스택
'''
스택을 구현하자
파이썬의 리스트는 링크드 리스트이면서, 스택의 연산을 지원한다.
'''

class Stack(list):
    def __init__(self):
        super().__init__()
        self.data_list = []
        self.data = None
                
    def push(self, data):
        self.data_list.append(data)
        
    def empty(self):
        if not self.data_list:
            return 1
        else:
            return 0

    def size(self):
        return len(self.data_list)
        
    def top(self):
        if not self.empty():
            return self.data_list[-1]
        else:
            return -1
    
    def pop(self):
        if not self.empty():
            return self.data_list.pop(-1)
        else:
            return -1
    
    def execute(self, input_commend, data):
        if input_commend == 'push':
            self.push(data)
        elif input_commend == 'empty':
            print(self.empty())
        elif input_commend == 'top':
            print(self.top())
        elif input_commend == 'pop':
            print(self.pop())
        else:
            print(self.size())
        # print(self.data_list)
        # print(data)
        # self.commend_dic = {'push':self.push(data), 'empty':self.empty(), 'top':self.top(), 'pop':self.pop(), 'size':self.size()}
        

        # if input_commend in self.commend_dic.keys():
        #     self.commend_dic[input_commend]
        #     print(f'executing:{input_commend}, data:{data}, result:{self.data_list}')
        #     if data is None:
        #         print(f'result:{self.commend_dic[input_commend]}')        

        
                


'''
test
'''
if __name__ == '__main__':
    import sys
    stack = Stack()    
    # stack.push(2)
    # print(stack.pop())
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        input_text = sys.stdin.readline().strip()
        try:
            commend, data = input_text.split()
        except:
            commend, data = input_text, None
        stack.execute(commend, data)