// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution {
    fun findPairs(nums: IntArray, k: Int): Int {
        if (k < 0) {
            return 0
        }

        val freq = nums.groupingBy { it }.eachCount()
        var pairs = 0
        for (num in freq.keys) {
            pairs += when {
                k == 0 && freq.getValue(num) > 1 -> 1
                k != 0 && freq.containsKey(num + k) -> 1
                else -> 0
            }
        }
        return pairs
    }
}
