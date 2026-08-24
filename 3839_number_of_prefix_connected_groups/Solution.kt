// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

class Solution {
    fun prefixConnected(words: Array<String>, k: Int): Int {
        var cnt = HashMap<String, Int>()
        for (w in words) {
            if (w.length >= k) {
                var p = w.substring(0, k)
                cnt[p] = cnt.getOrDefault(p, 0 + 1)
            }
        }
        var ans = 0
        for (v in cnt.values) { if (v > 1) ans++ }
        return ans
    }
}
