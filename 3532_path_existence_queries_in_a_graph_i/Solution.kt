// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

class Solution {
    fun pathExistenceQueries(n: Int, nums: IntArray, maxDiff: Int, queries: Array<IntArray>): BooleanArray {
        var g = IntArray(n)
        var cnt = 0
        for (i in 1 until n) {
            if (nums[i] - nums[i - 1] > maxDiff) cn{ t = t + 1 }
            g[i] = cnt
        }
        var ans = BooleanArray(queries.size)
        var i: Int = 0
while (i < queries.length) {

            ans[i] = g[queries[i][0]] == g[queries[i][1]]
        return ans
    }
}
i = i + 1
}
