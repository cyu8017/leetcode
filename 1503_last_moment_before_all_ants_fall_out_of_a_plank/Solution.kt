// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

class Solution {
    fun getLastMoment(n: Int, left: IntArray, right: IntArray): Int {
        var maxLeft = 0
        for (pos in left) maxLeft = maxOf(maxLeft, pos)
        var minRight = n
        for (pos in right) minRight = minOf(minRight, pos)
        return maxOf(maxLeft, n - minRight)
    }
}
