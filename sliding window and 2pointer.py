"""
Longest Substring Without Repeating Characters
Max Consecutive Ones III
Fruit Into Baskets
longest repeating character replacement
Binary subarray with sum
Count number of nice subarrays
Number of substring containing all three characters
Maximum point you can obtain from cards
longest Substring with At Most K Distinct Characters
Subarray with k different integers
Minimum Window Substring
Minimum Window Subsequence

"""
class Swand2p:
    #medium problems
    #"abcda" right pointer is moving when r sees a duplicate l shifts to the next to avoid duplicate
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash=[-1]*256
        l=0
        r=0
        mlen=0
        while(r<len(s)):
            if hash[ord(s[r])]!=-1 and hash[ord(s[r])]>=l:
                l=hash[ord(s[r])]+1
            mlen=max(r-l+1,mlen)
            hash[ord(s[r])]=r
            r+=1
        return mlen
    
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        r=0
        z=0
        mlen=0
        while(r<len(nums)):
            if nums[r]==0:
                z+=1
            while(z>k):
                if nums[l]==0:
                    z-=1
                l+=1
            if z<=k:
                mlen=max(mlen,r-l+1)
            r+=1
        return mlen
    
    def totalElements(self,arr):
        l=0
        r=0
        dk={}
        maxlen=0
        while(r<len(arr)):
            dk[arr[r]]=dk.get(arr[r],0)+1
            if(len(dk)>2):
                while(len(dk)>2):
                    if arr[l] in dk:
                        dk[arr[l]]-=1
                        if dk[arr[l]]==0:
                            del dk[arr[l]]
                    l+=1
            if len(dk)<=2:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
    
    def characterReplacement(self, s: str, k: int) -> int:
        dk={}
        l=0;maxf=0;ans=0
        for r in range(len(s)):
            dk[s[r]]=dk.get(s[r],0)+1
            maxf=max(maxf,dk[s[r]])
            while (r-l+1) - maxf > k:
                dk[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
    
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def ans(arr,goal):
            l=0;r=0;scum=0;cunt=0
            if goal<0:
                return 0
            while(r<len(arr)):
                scum+=arr[r]
                while(scum>goal):
                    scum-=arr[l]
                    l+=1
                cunt+=(r-l+1)
                r+=1
            return cunt
        return ans(nums,goal)-ans(nums,goal-1)
    
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def ans(arr,goal):
            l=0;r=0;scum=0;cunt=0
            if goal<0:
                return 0
            while(r<len(arr)):
                scum+=(arr[r])%2
                while(scum>goal):
                    scum-=(arr[l])%2
                    l+=1
                cunt+=(r-l+1)
                r+=1
            return cunt
        return ans(nums,k)-ans(nums,k-1)
    def numberOfSubstrings(self, s: str) -> int:
        ans=[-1,-1,-1]
        cunt=0
        for i in range(len(s)):
            ans[ord(s[i])-ord('a')]=i
            cunt=cunt+(1+min(ans[0],ans[1],ans[2]))
        return cunt
    
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        lsum=0;rsum=0;l=0;r=len(cardPoints)-1;msum=0
        while(l<k):
            lsum+=cardPoints[l]
            l+=1
        l-=1
        msum+=lsum
        while(l>=0):
            lsum-=cardPoints[l]
            rsum+=cardPoints[r]
            l-=1
            r-=1
            msum=max(msum,lsum+rsum)
        return msum
    #hard problems
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def ans(arr,goal):
            l=0;r=0;scum={};cunt=0
            while(r<len(arr)):
                scum[arr[r]]=scum.get(arr[r],0)+1
                while(len(scum)>goal):
                    scum[arr[l]]=scum[arr[l]]-1
                    if scum[arr[l]]==0:
                        del scum[arr[l]]
                    l+=1
                cunt+=(r-l+1)
                r+=1
            return cunt
        return ans(nums,k)-ans(nums,k-1)
    def longestsubstringwithKDistinct(self,s,k):
        dk={}
        maxlen=0
        l=r=0
        while(r<len(s)):
            dk[s[r]]=dk.get(s[r],0)+1
            while(len(dk)>k):
                dk[s[l]]-=1
                if dk[s[l]]==0:
                    del dk[s[l]]
                l+=1
            if len(dk)<=k:
                maxlen=max(r-l+1,maxlen)
            r+=1
        return maxlen
            
    
obj=Swand2p()
