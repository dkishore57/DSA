"""
1.recursive implementation of atoi()
2.pow(x,n)
3.count good numbers
4.sort a stack using recursion
5.reverse a stack using recursion
6.generate all binary strings
7.generate paranthesis
8.print all sub sequences/power set
9.learn all patterns of sub sequences
10.count all sub sequences with sum k
11.check if there exists a sub sequence with sum k
12.combination sum
13.combination sum-2
14.subset sum-1
15.subset sum-2
16.combination sum-3
17.letter combinations of a phone number 
18.palindrome partitioning
19.word search
20.n queen
21.rat in maze
22.word break
23.m coloring problem
24.sudoku solver
25.expression add operators
"""
class recursion():
    def recursive_reverse(self,arr,ind,):
        if ind>=len(arr)//2:
            return arr
        arr[ind],arr[len(arr)-ind-1]=arr[len(arr)-ind-1],arr[ind]
        return self.recursive_reverse(arr,ind+1)
    def check_pali(self,str1,ind):
        if ind>=len(str1)//2:
            return 1
        if str1[ind]!=str1[len(str1)-ind-1]:
            return 0
        return self.check_pali(str1,ind+1)
    def subsequence(self,ind,arr,temp,n,ANS):
        if ind==n:
            ANS.append(temp[:])
            return 
        temp.append(arr[ind])
        self.subsequence(ind+1,arr,temp,n,ANS)
        temp.pop()
        self.subsequence(ind+1,arr,temp,n,ANS)
    def powe(self,x,n):
        ans = 1.0
        nn = n
        if nn < 0:
            nn = -1 * nn
        while nn:
            if nn % 2:
                ans = ans * x
                nn = nn - 1
            else:
                x = x * x
                nn = nn // 2
        if n < 0:
            ans = 1.0 / ans
        return ans
    
obj=recursion()
"""
rev=obj.recursive_reverse([1,3,4,5],0)
check_pali=obj.check_pali("MADAM",0)
ANS=[]
sub=obj.subsequence(0,[1,2,3],[],3,ANS)"""
powe=obj.powe(2,4)
print(powe)

        
