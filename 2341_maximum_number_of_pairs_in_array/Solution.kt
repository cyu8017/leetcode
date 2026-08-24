// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

class Solution {
    fun numberOfPairs(nums: IntArray): IntArray {
        val cnt = HashMap<Int, Int>()
        for (x in nums) cnt[x] = cnt.getOrDefault(x, 0) + 1
        var pairs = 0
        var left = 0
        for (c in cnt.values) {
            pairs += c / 2
            left += c % 2
        }
        return intArrayOf(pairs, left)
    }
}
