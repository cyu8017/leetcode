// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

class Solution {
    fun isPossibleToSplit(nums: IntArray): Boolean {
        var cnt = IntArray(101)
        for (x in nums) {
            cnt[x]++
            if (cnt[x] >= 3) return false
        }
        return true
    }
}
