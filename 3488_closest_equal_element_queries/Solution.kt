// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

class Solution {
    fun solveQueries(nums: IntArray, queries: IntArray): IntArray {
        var n = nums.size
        var pos = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) { pos.getOrPut(nums[i]) { ArrayList() }.add(i) }
        var ans = IntArray(queries.size)
        for (qi in 0 until queries.size) {
            var idx = queries[qi]
            var x = nums[idx]
            var arr = pos[x]
            if (arr.size == 1) { ans[qi] = -1; continue; }
            var best = n
            for (p in arr) {
                if (p == idx) continue
                var d = kotlin.math.abs(p - idx)
                d = minOf(d, n - d)
                if (d < best) best = d
            }
            ans[qi] = best
        }
        return ans
    }
}
