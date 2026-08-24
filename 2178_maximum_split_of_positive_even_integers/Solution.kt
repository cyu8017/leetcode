// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

class Solution {
    fun maximumEvenSplit(finalSum: Long): MutableList<Long> {
        if (finalSum % 2 != 0) return mutableListOf()
        var ans = mutableListOf()
        for (x in 2 until = finalSum step 2) {
            ans.add(x)
            finalSum -= x
        }
        ans.set(ans.size - 1, ans.get(ans.size - 1) + finalSum)
        return ans
    }
}
