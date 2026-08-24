// LeetCode 3036 - Number of Subarrays That Match a Pattern II
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

class Solution {
    fun countMatchingSubarrays(nums: IntArray, pattern: IntArray): Int {
        var N = pattern.size
        var ps = IntArray(N + 1)
        ps[0] = -1
        ps[1] = 0
        for (i in 2, p = 0..N) {
            var x = pattern[i - 1]
            while (p >= 0 && pattern[p] != x) p = ps[p]
            p++
            ps[i] = p
        }
        var res = 0
        var M = nums.size
        for (i in 1, p = 0 until M) {
            var t = nums[i] - nums[i - 1]
            if (t > 0) t = 1
            else if (t < 0) t = -1
            while (p >= 0 && pattern[p] != t) p = ps[p]
            if (++p == N) {
                res++
                p = ps[p]
            }
        }
        return res
    }
}
