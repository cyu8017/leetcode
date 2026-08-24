// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

class Solution {
    fun findMaximalUncoveredRanges(n: Int, ranges: Array<IntArray>): Array<IntArray> {
        ranges.sortBy { it[0] }
        val ans = ArrayList<IntArray>()
        var cur = 0
        for (r in ranges) {
            if (r[0] > cur) ans.add(intArrayOf(cur, r[0] - 1))
            if (r[1] + 1 > cur) cur = r[1] + 1
        }
        if (cur < n) ans.add(intArrayOf(cur, n - 1))
        return ans.toTypedArray()
    }
}
