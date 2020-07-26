import sys
def getMinJump(arr,start,end):
    if(start == end):
        return 0
    
    if(arr[start]==0):
        return float('inf')
    
    min = float('inf')
    for i in range(start+1,end+1):
        if(i<start+arr[start]+1):
            jump = getMinJump(arr,i,end)
            if(jump != float('inf') and jump+1<min):
                min = jump+1
    return min



if __name__ == "__main__":
    n = int(input())
    jumpArr = list(map(int,input().split()))
    
    if(len(jumpArr)>1000 or jumpArr[0]==0):
        print(-1)
        sys.exit(0)
    for element in jumpArr:
        if(element>100 or element==0):
            print(-1)
            sys.exit(0)
    if(getMinJump(jumpArr,0,n-1)!=float('inf')):
        print(getMinJump(jumpArr,0,n-1))
    else:
        print(-1)