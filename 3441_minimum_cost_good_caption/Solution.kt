// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

class Solution {
    fun minCostGoodCaption(caption: String): String {
        var n = caption.length
        if (n < 3) return ""
        var ans = caption.toCharArray()
        var i = 0
        while (i < n) {
            var j = i
            while (j < n && ans[j] == ans[i]) j++
            if (j - i >= 3) { i = j; continue; }
            var need = 3 - (j - i)
            if (j + need <= n) {
                for (t in 0 until need) { ans[j + t] = ans[i] }
                i = j + need
            } else {
                var ch = 'a'
                if (i > 0) ch = ans[i - 1]
                else if (j < n) ch = caption[j]
                for (t in i until n) { ans[t] = ch }
                break
            }
        }
        i = 0
        while (i < n) {
            var j = i
            while (j < n && ans[j] == ans[i]) j++
            if (j - i < 3) return ""
            i = j
        }
        return String(ans)
    }
}
