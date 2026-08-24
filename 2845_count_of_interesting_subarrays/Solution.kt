// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

class Solution {
    fun countInterestingSubarrays(nums: List<Int>, modulo: Int, k: Int): Long {
        val freq = HashMap<Int, Int>()
        freq[0] = 1
        var ans = 0L
        var pref = 0
        for (v in nums) {
            if (v % modulo == k) pref++
            var need = (pref - k) % modulo
            if (need < 0) need += modulo
            ans += freq.getOrDefault(need, 0)
            val key = pref % modulo
            freq[key] = freq.getOrDefault(key, 0) + 1
        }
        return ans
    }
}
