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
    
obj=Swand2p()
lengthOfLongestSubstring=obj.lengthOfLongestSubstring("abcabcbb")
longestOnes=obj.longestOnes([1,0,0,1,1,0,1],2)
print(longestOnes)