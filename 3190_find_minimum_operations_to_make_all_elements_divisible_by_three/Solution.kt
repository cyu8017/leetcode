// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution {
    fun minimumOperations(nums: IntArray): Int {
        var ans = 0
        for (x in nums) { if (x % 3 != 0) ans++ }
        return ans
    }
}
