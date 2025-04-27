import random
import numpy as np

card_marks = 'star,sun,moon'
marks = card_marks.split(',')
print(marks)
print('moonは' + str(marks.index('moon')) + '番目')
print(marks[-2])

def main() -> None:
    #等確率でひとつ選ぶ。
    mark = random.choice(marks)
    print(mark)
    #等確率で２つ選ぶ。
    num_trial = 2
    mark_2 = np.random.choice(marks, num_trial)
    print(mark_2)
    #確率を指定して３つ選ぶ。
    num_trial = 3
    prob = [1/5,1/5,3/5]
    mark_3 = np.random.choice(marks, num_trial, p = prob)
    print(mark_3)
    
    #並べ替え
    marks.sort()
    print(marks)
    #starを取り除く。
    marks.remove('star')
    print(marks)

if __name__ == '__main__':
    main()