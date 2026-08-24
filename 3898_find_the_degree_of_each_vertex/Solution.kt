// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

class Solution {
    fun findDegrees(matrix: Array<IntArray>): IntArray {
        var ans = IntArray(matrix.size)
        for (i in 0 until matrix.size) {
            for (x in matrix[i]) { ans[i] += x }
        }
        return ans
    }
}
