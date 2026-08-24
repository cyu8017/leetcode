// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution {
    fun isReachableAtTime(sx: Int, sy: Int, fx: Int, fy: Int, t: Int): Boolean {
        var need = maxOf(kotlin.math.abs(sx - fx), kotlin.math.abs(sy - fy))
        if (need == 0) return t != 1
        return t >= need
    }
}
