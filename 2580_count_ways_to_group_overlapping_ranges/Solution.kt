// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution {
    fun countWays(ranges: Array<IntArray>): Int {
        val MOD = 1_000_000_007
        ranges.sortBy { it[0] }
        var groups = 0
        var end = -1
        for (r in ranges) {
            if (r[0] > end) {
                groups += 1
                end = r[1]
            } else if (r[1] > end) {
                end = r[1]
            }
        }
        var ans = 1
        repeat(groups) { ans = ans * 2 % MOD }
        return ans
    }
}
