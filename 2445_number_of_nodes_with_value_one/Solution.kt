// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

class Solution {
    fun numberOfNodes(n: Int, queries: IntArray): Int {
        val flip = IntArray(n + 1)
        val values = IntArray(n + 1)
        for (q in queries) flip[q] = flip[q] xor 1
        var ans = 0
        for (i in 1..n) {
            values[i] = flip[i]
            if (i > 1) values[i] = values[i] xor values[i / 2]
            ans += values[i]
        }
        return ans
    }
}
