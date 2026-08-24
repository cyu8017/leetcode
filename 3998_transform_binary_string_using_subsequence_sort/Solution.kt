// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

class Solution {
    fun transformStr(s: String, strs: Array<String>): BooleanArray {
        val n = s.length
        val prefix = IntArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + if (s[i] == '1') 1 else 0
        }
        val result = BooleanArray(strs.size)
        for (i in strs.indices) {
            var left = 0
            var right = 0
            var ok = true
            for (j in 0 until n) {
                left += if (strs[i][j] == '1') 1 else 0
                val add = if (strs[i][j] != '0') 1 else 0
                right += add
                if (right > prefix[j + 1]) right = prefix[j + 1]
                if (left > right) {
                    ok = false
                    break
                }
            }
            result[i] = ok && left <= prefix[n] && prefix[n] <= right
        }
        return result
    }
}
