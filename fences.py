numFences = int(input())
heights = input().split(' ')
widths = input().split(' ')
#we want to average of heights * width
areaSum  = 0
for i in range(numFences):
    area = (int(heights[i]) + int(heights[i+1]))/2  * int(widths[i])
    areaSum += area

print(areaSum)