// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

class Solution {
    fun escapeGhosts(ghosts: Array<IntArray>, target: IntArray): Boolean {
        var targetDist = kotlin.math.abs(target[0]) + kotlin.math.abs(target[1])
        for (ghost in ghosts) {
            if (kotlin.math.abs(ghost[0] - target[0]) + kotlin.math.abs(ghost[1] - target[1]) <= targetDist) {
                return false
            }
        }
        return true
    }
}
