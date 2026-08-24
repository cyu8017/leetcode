// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

class Solution {
    fun maxValue(n: Int, restrictions: Array<IntArray>, diff: IntArray): Int {
        val INF = Int.MAX_VALUE / 4
        var bound = IntArray(n)
        for (i in 0 until n) { bound[i] = INF }
        bound[0] = 0
        for (r in restrictions) bound[r[0]] = r[1]
        for (i in 1 until n) { bound[i] = minOf(bound[i], bound[i - 1] + diff[i - 1]) }
        run {
            var i = n - 2
            while (i >= 0) {
                bound[i] = minOf(bound[i], bound[i + 1] + diff[i])
                i = i - 1
            }
        }
        var ans = bound[0]
        for (i in 1 until n) { ans = maxOf(ans, bound[i]) }
        return ans
    }
}
