// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution {
    fun repeatedNTimes(nums: IntArray): Int {
        var seen = HashSet()
        for (x in nums) {
            if (seen.contains(x)) return x
            seen.add(x)
        }
        return -1
    }
}
