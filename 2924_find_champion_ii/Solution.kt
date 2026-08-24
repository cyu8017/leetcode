// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

class Solution {
    fun findChampion(n: Int, edges: Array<IntArray>): Int {
        var indeg = IntArray(n)
        for (e in edges) { indeg[e[1]]++ }
        var ans = -1
        for (i in 0 until n) {
            if (indeg[i] == 0) {
                if (ans != -1) return -1
                ans = i
            }
        }
        return ans
    }
}
