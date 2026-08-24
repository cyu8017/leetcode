// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

class Solution {
    fun cycleLengthQueries(n: Int, queries: Array<IntArray>): IntArray {
            var ans: IntArray = IntArray(queries.size)
            var i: Int = 0
    while (i < queries.size) {
    
                var a: Int = queries[i][0]
                var b: Int = queries[i][1]
                var steps: Int = 0
                while (a != b) {
                    if (a > b) a /= 2
                    else b /= 2
                    steps = steps + 1
                }
                ans[i] = steps + 1
    
    i = i + 1
    }
            return ans
    }
}
