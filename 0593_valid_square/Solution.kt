// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/


class Solution {
    fun validSquare(p1: IntArray, p2: IntArray, p3: IntArray, p4: IntArray): Boolean {
        val dists = longArrayOf(dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4))
        dists.sort()
        return dists[0] > 0 && dists[0] == dists[1] && dists[1] == dists[2] && dists[2] == dists[3]
            && dists[4] == dists[5] && dists[4] == 2 * dists[0]
    }

    private fun dist(a: IntArray, b: IntArray): Long {
        val dx = (a[0] - b[0]).toLong()
        val dy = (a[1] - b[1]).toLong()
        return dx * dx + dy * dy
    }
}
