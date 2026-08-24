// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

class Solution {
    fun countTheNumOfKFreeSubsets(nums: IntArray, k: Int): Long {
        nums.sort()
        val groups = HashMap<Int, MutableList<Int>>()
        for (x in nums) groups.getOrPut(x % k) { ArrayList() }.add(x)
        var ans = 1L
        for (g in groups.values) {
            var prevVal = -1
            var prevTake = 0L
            var prevSkip = 1L
            for (v in g) {
                val skip = prevTake + prevSkip
                val take = if (prevVal + k == v) prevSkip else prevTake + prevSkip
                prevTake = take
                prevSkip = skip
                prevVal = v
            }
            ans *= prevTake + prevSkip
        }
        return ans
    }
}
