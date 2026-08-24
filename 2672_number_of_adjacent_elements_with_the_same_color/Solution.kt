// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution {
    fun colorTheArray(n: Int, queries: Array<IntArray>): IntArray {
        val colors = IntArray(n)
        val ans = IntArray(queries.size)
        var same = 0
        for (i in queries.indices) {
            val idx = queries[i][0]
            val color = queries[i][1]
            if (colors[idx] != 0) {
                if (idx > 0 && colors[idx] == colors[idx - 1]) same--
                if (idx + 1 < n && colors[idx] == colors[idx + 1]) same--
            }
            colors[idx] = color
            if (idx > 0 && colors[idx] == colors[idx - 1]) same++
            if (idx + 1 < n && colors[idx] == colors[idx + 1]) same++
            ans[i] = same
        }
        return ans
    }
}
