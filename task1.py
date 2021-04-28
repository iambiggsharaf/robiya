
myArray = [
    [100, 500, 600],
    [900],
    [5, 7],
    [1, 2 ,3], 
    [1, 2, 3],
]


# a function checks that number
# is or not a Prime number
def isPrime(number):

    flag = True
    if number > 1:
        # we will go just till
        # half of our number 
        # because no number have 
        # divisor after half of it
        for i in range(2, number // 2):
             if number % i == 0:
                # found divisor, then it's a composite number
                flag = False
                break
        
        # checking do we found a composite number or not:
        if flag == False:
            return False
        elif flag == True:
            return True


def onlyPrimesList(arr):
    flag = True

    for i in arr:
        for j in i:
            if isPrime(j) == False:
                flag = False
                break
        if flag == False:
            flag = True
        elif flag == True:
            return "YES! , There is one:", i
            break

        
def countPairs(arr):
 
    ans = 0
 
    for i in range(0 , len(arr)):
        for j in range(i + 1, len(arr)):
 
            # finding the index
            # with same value but
            # different index.
            if (arr[i] == arr[j]):
                ans += 1    

    return ans

  
def maxElementInLongestList(arr):

   longestList = []
   maxLength = max(len(x) for x in arr)

   for i in arr:

      if len(i) == maxLength:
         longestList = i
         break

   return max(longestList)




print(onlyPrimesList(myArray))
print(countPairs(myArray))
print(maxElementInLongestList(myArray))
 
                




            

