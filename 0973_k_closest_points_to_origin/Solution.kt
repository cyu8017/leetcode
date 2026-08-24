// LeetCode 0973 - K Closest Points to Origin
// https://leetcode.com/problems/k-closest-points-to-origin/

class Solution {
    fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> {
        points.sortBy { it[0] * it[0] + it[1] * it[1] }
        return points.copyOf(k)
    }
}
