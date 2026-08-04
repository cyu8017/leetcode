// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

class Solution {
    fun distinctEchoSubstrings(text: String): Int {
        val n = text.length
        val mod1 = 1_000_000_007L
        val mod2 = 1_000_000_009L
        val base = 911382323L
        val h1 = LongArray(n + 1)
        val h2 = LongArray(n + 1)
        val p1 = LongArray(n + 1) { 1 }
        val p2 = LongArray(n + 1) { 1 }
        for (i in text.indices) {
            val code = text[i].code.toLong()
            h1[i + 1] = (h1[i] * base + code) % mod1
            h2[i + 1] = (h2[i] * base + code) % mod2
            p1[i + 1] = p1[i] * base % mod1
            p2[i + 1] = p2[i] * base % mod2
        }
        fun hashed(left: Int, right: Int): Pair<Long, Long> {
            val length = right - left
            val a = ((h1[right] - h1[left] * p1[length]) % mod1 + mod1) % mod1
            val b = ((h2[right] - h2[left] * p2[length]) % mod2 + mod2) % mod2
            return a to b
        }
        val echoes = mutableSetOf<Triple<Int, Long, Long>>()
        for (half in 1..n / 2) {
            for (left in 0..n - 2 * half) {
                if (hashed(left, left + half) == hashed(left + half, left + 2 * half)) {
                    val h = hashed(left, left + 2 * half)
                    echoes.add(Triple(2 * half, h.first, h.second))
                }
            }
        }
        return echoes.size
    }
}
