// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

class Solution {
    fun maxSum(grid: Array<IntArray>, limits: IntArray, k: Int): Long {
        var h = PriorityQueue<Int>()
        var sum = 0
        for (i in 0 until grid.size) {
            var r = grid[i].clone()
            r.sort()
            var lim = limits[i]
            if (lim > r.size) lim = r.size
            for (j in 0 until lim) {
                var `val` = r[r.size - 1 - j]
                h.offer(val)
                sum += val
                if (h.size > k) sum -= h.poll()
            }
        }
        return sum
    }
}
