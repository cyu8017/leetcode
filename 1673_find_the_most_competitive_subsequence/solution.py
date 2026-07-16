class Solution:
    def mostCompetitive(self, nums, k):
        st=[]
        for i,x in enumerate(nums):
            while st and st[-1]>x and len(st)-1+len(nums)-i>=k:st.pop()
            if len(st)<k:st.append(x)
        return st
