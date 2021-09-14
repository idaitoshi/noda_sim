import random
import numpy as np
import matplotlib.pyplot as plt

# https://twitter.com/madnoda/status/1437361820176568320?s=20

# 1000人に対して1万円の受け渡しを1000回行う
def shuffle(array):
    for x in range(1000):
        i = random.randrange(0,999,1)
        j = random.randrange(0,999,1)
        if(0 < array[j]):
            array[j] = array[j] -1
            array[i] = array[i] + 1
    # for loop end
    return(array)

def save_plt(array,x):
    figure, ax = plt.subplots()
    figure.set_figheight(24)
    figure.set_figwidth(36)
    plt.clf()
    plt.xlim(0, 300)
    plt.ylim(0, 300)
    plt.hist(np.array(array),bins=300)
    figure.savefig("img{:03d}.png".format(x+1))
#func end


#1000人に100万円を配る(1万円単位)
array = []
for x in range(1000):
    array.append(100)

#描画領域の初期化


# 初期状態を保存
save_plt(array,0)

# 300回シャッフルしながら画像を生成
for x in range(600):
    print(x)
    array = shuffle(array)
    save_plt(array,x+1)
