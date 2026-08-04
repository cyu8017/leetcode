// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution {
    fun numberOfSubarrays(nums: IntArray, k: Int): Int {
        val freq = mutableMapOf(0 to 1)
        var odd = 0
        var answer = 0
        for (x in nums) {
            odd += x and 1
            answer += freq.getOrDefault(odd - k, 0)
            freq[odd] = freq.getOrDefault(odd, 0) + 1
        }
        return answer
    }
}
