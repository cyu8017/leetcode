// LeetCode 1946
// https://leetcode.com/problems/largest-number-after-mutating-substring/

class Solution {
    fun maximumNumber(num: String, change: IntArray): String {
        val chars = num.toCharArray()
        var started = false
        for (i in chars.indices) {
            val d = chars[i] - '0'
            val mapped = change[d]
            if (mapped > d) {
                chars[i] = ('0' + mapped)
                started = true
            } else if (mapped < d && started) break
        }
        return String(chars)
    }
}
