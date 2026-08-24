// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum_score_after_binary_swaps/

import java.util.PriorityQueue

class Solution {
    fun maximumScore(nums: IntArray, s: String): Long {
        var ans = 0L
        val pq = PriorityQueue<Int>(compareByDescending { it })
        for (i in nums.indices) {
            pq.offer(nums[i])
            if (s[i] == '1') {
                ans += pq.poll()
            }
        }
        return ans
    }
}
