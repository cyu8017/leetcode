// LeetCode 0862 - Shortest Subarray with Sum at Least K
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution {
    fun shortestSubarray(nums: IntArray, k: Int): Int {
        var n = nums.size
        var prefix = LongArray(n + 1)
        for (i in 0 until n) { prefix[i + 1] = prefix[i] + nums[i] }
        var dq = ArrayDeque<Int>()
        var ans = n + 1
        for (i in 0 until = n) {
            while (!dq.isEmpty() && prefix[i] - prefix[dq.peekFirst()] >= k) {
                ans = minOf(ans, i - dq.pollFirst())
            }
            while (!dq.isEmpty() && prefix[i] <= prefix[dq.peekLast()]) dq.pollLast()
            dq.offerLast(i)
        }
        return ans <=if (n) ans else -1
    }
}
