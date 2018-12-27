import matplotlib
matplotlib.use('Agg')

import elice_utils
import matplotlib.pyplot as plt
import random
import numpy as np
import random as rand

def getStatistics(data) :
    average = sum(data)/len(data) 
#    print(sum(data))
#    print(len(data))
 #   print(average)
 #   print(data)
    data = np.array(data)
#    print(data)
    central_data = data-float(average)
#    print(central_data)
    squared_data = central_data**2
#    print(squared_data)
    variance = sum(squared_data) / len(squared_data)

    return (average, variance)

def doSample(n, m) :
    result = []
    for i in range(m):
        result.append(rand.randrange(1,n+1))
#    print(result)
    '''
    1 ~ n 까지의 수를 균일 분포를 따라 m회 추출한 결과를 리스트로 반환하는 함수를 작성합니다.
    예를 들어, n = 10, m = 3 일 경우에는 1 ~ 10 까지의 수를 균일 분포에 따라 3회 추출하므로
    가능한 결과로 [1, 8, 5] 가 있을 수 있습니다. 물론, 추출을 할 때마다 그 결과가 달라질 수 있습니다.
    '''
    return result

def plotResult(data) :
    frequency = [ 0 for i in range(max(data)+1) ]

    for element in data :
        frequency[element] += 1

    n = len(frequency)

    myRange = range(1, n)
    width = 1

    plt.bar(myRange, frequency[1:])

    plt.xlabel("Sample", fontsize=20)
    plt.ylabel("Frequency", fontsize=20)
    
    filename = "chart.svg"
    plt.savefig(filename)
    elice_utils.send_image(filename)

    plt.close()

def main():
    line = [int(x) for x in input("입력 > ").split()]
    
    n = line[0]
    m = line[1]

    result = doSample(n, m)

    plotResult(result)
    
    stat = getStatistics(result)

    print(str(stat[0]) + " " + str(stat[1]))

if __name__ == "__main__":
    main()

