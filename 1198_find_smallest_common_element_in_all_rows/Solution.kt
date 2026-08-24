// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

class Solution {
    fun smallestCommonElement(mat: Array<IntArray>): Int {
        var common = mat[0].toMutableSet()
        for (r in 1 until mat.size) {
            common = common.intersect(mat[r].toSet()).toMutableSet()
            if (common.isEmpty()) return -1
        }
        return common.minOrNull() ?: -1
    }
}
