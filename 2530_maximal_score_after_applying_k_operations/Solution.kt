// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class Solution {
    fun maxKelements(nums: IntArray, k: Int): Long {
        var pq = PriorityQueue((a, b) -> (b).compareTo(a))
        for (x in nums) { pq.offer(x) }
        var ans = 0
        for (i in 0 until k) {
            var x = pq.poll()
            ans += x
            pq.offer((x + 2) / 3)
        }
        return ans
    }
}
