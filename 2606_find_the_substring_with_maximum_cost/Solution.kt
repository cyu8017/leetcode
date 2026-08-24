// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution {
    fun maximumCostSubstring(s: String, chars: String, vals: IntArray): Int {
        var `val` = IntArray(26)
        for (i in 0 until 26) { val[i] = i + 1 }
        for (i in 0 until chars.length) { val[chars[i] - 'a'] = vals[i] }
        var best = 0
        var cur = 0
        for (c in s.toCharArray()) {
            cur += val[c - 'a']
            if (cur < 0) cur = 0
            if (cur > best) best = cur
        }
        return best
    }
}
