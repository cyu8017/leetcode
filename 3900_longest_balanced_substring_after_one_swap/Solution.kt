// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

class Solution {
    fun longestBalanced(s: String): Int {
        var cnt0 = 0
        for (c in s.toCharArray()) { if (c == '0') cnt0++ }
        var cnt1 = s.length - cnt0
        var pos = HashMap<Int, MutableList<Int>>()
        pos[0] = ArrayList(List.of(-1))
        var ans = 0
        var pre = 0
        for (i in 0 until s.length) {
            if (s[i] == '1') pre++
            else pre--
            pos.computeIfAbsent(pre, k -> ArrayList()).add(i)
            ans = maxOf(ans, i - pos[pre][0])
            if (pos.containsKey(pre - 2)) {
                var p = pos[pre - 2]
                if ((i - p[0] - 2) / 2 < cnt0) ans = maxOf(ans, i - p[0])
                else if (p.size > 1) ans = maxOf(ans, i - p[1])
            }
            if (pos.containsKey(pre + 2)) {
                var p = pos[pre + 2]
                if ((i - p[0] - 2) / 2 < cnt1) ans = maxOf(ans, i - p[0])
                else if (p.size > 1) ans = maxOf(ans, i - p[1])
            }
        }
        return ans
    }
}
