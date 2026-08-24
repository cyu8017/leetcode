// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        var seen = HashSet<Int>()
        for (x in nums) {
            if (x < k) return -1
            if (x > k) seen.add(x)
        }
        return seen.size
    }
}
