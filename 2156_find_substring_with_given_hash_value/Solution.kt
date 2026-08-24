// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

class Solution {
    fun subStrHash(s: String, power: Int, modulo: Int, k: Int, hashValue: Int): String {
        var n: Int = s.length
        var pk: Long = 1
        for (i in 0 until k - 1) pk = pk * power % modulo
        var h: Long = 0
        var ans: Int = 0
        for (i in n - 1 downTo n - k)
            h = (h * power + (s[i] - 'a' + 1)) % modulo
        if (h == hashValue) ans = n - k
        for (i in n - k - 1 downTo 0) {
            h = (h - (s[i + k] - 'a' + 1) * pk % modulo + modulo) % modulo
            h = (h * power + (s[i] - 'a' + 1)) % modulo
            if (h == hashValue) ans = i
        }
        return s.substring(ans, ans + k)
    }
}
