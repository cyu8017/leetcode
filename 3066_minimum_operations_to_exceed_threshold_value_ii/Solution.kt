// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        var pq = PriorityQueue<Long>()
        for (x in nums) { pq.offer(x) }
        var ans = 0
        while (pq.size > 1 && pq.peek() < k) {
            var x = pq.poll()
            var y = pq.poll()
            pq.offer(x * 2 + y)
            ans++
        }
        return ans
    }
}
