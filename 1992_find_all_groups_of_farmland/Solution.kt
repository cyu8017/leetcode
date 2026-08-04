// LeetCode 1992
// https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution {
    fun findFarmland(land: Array<IntArray>): Array<IntArray> {
        val m = land.size
        val n = land[0].size
        val ans = mutableListOf<IntArray>()
        for (i in 0 until m) for (j in 0 until n) {
            if (land[i][j] == 1 && (i == 0 || land[i - 1][j] == 0) && (j == 0 || land[i][j - 1] == 0)) {
                var r = i
                var c = j
                while (r + 1 < m && land[r + 1][j] == 1) r++
                while (c + 1 < n && land[i][c + 1] == 1) c++
                ans.add(intArrayOf(i, j, r, c))
            }
        }
        return ans.toTypedArray()
    }
}
