// LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

class Solution {
    fun executeInstructions(n: Int, startPos: IntArray, s: String): IntArray {
        var m: Int = s.length
        var ans: IntArray = IntArray(m)
        for (i in 0 until m) {
            var r: Int = startPos[0], c = startPos[1], cnt = 0
            for (j in i until m) {
                var ch: Char = s[j]
                if (ch == 'L') c--
                else if (ch == 'R') c++
                else if (ch == 'U') r--
                else r++
                if (r < 0 || r >= n || c < 0 || c >= n) break
                cnt++
            }
            ans[i] = cnt
        }
        return ans
    }
}
