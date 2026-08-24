// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution {
    fun subarraysDivByK(nums: IntArray, k: Int): Int {
        var count = HashMap()
        count.put(0, 1)
        var prefix = 0
        var ans = 0
        for (x in nums) {
            prefix = ((prefix + x) % k + k) % k
            ans += count.getOrDefault(prefix, 0)
            count.put(prefix, count.getOrDefault(prefix, 0) + 1)
        }
        return ans
    }
}
