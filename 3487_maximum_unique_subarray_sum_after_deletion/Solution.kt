// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

class Solution {
    fun maxSum(nums: IntArray): Int {
        var seen = HashSet<Int>()
        var sum = 0
        var hasPos = false
        var maxNeg = (-1e9)
        for (x in nums) {
            if (x < 0) {
                if (x > maxNeg) maxNeg = x
                continue
            }
            hasPos = true
            if (seen.add(x)) sum += x
        }
        return if (hasPos) sum else maxNeg
    }
}
