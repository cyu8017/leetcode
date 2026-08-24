// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

class Solution {
    fun mirrorFrequency(s: String): Int {
        var freq = HashMap<Char, Int>()
        for (c in s.toCharArray()) { freq[c] = freq.getOrDefault(c, 0 + 1) }
        var ans = 0
        var vis = HashMap<Char, Boolean>()
        for (kv in freq) {
            var c = kv.key
            var v = kv.value
            var m: Char? = null
            if (c >= 'a' && c <= 'z') m = (char) ('a' + 25 - (c - 'a'))
            else m = (char) ('0' + (9 - (c - '0')))
            if ((Boolean.TRUE == vis[m])) continue
            vis[c] = true
            var mv = freq.getOrDefault(m, 0)
            ans += kotlin.math.abs(v - mv)
        }
        return ans
    }
}
