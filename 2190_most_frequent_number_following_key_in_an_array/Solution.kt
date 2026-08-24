// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution {
    fun mostFrequent(nums: IntArray, key: Int): Int {
        var freq = HashMap()
        var best: Int = 0, ans = 0
        var i = 0
        while (i + 1 < nums.size) {
            if (nums[i] == key) {
                var v: Int = freq.merge(nums[i + 1], 1, Int::sum)
                if (v > best) { best = v; ans = nums[i + 1]; }
                i++
            }
        }
        return ans
    }
}
