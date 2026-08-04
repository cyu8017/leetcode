// LeetCode 1363 - Largest Multiple of Three
// https://leetcode.com/problems/largest-multiple-of-three/

class Solution {
    fun largestMultipleOfThree(digits: IntArray): String {
        val cnt = IntArray(10)
        var rem = 0
        for (d in digits) {
            cnt[d]++
            rem += d
        }
        rem %= 3
        fun remove(r: Int, k0: Int): Boolean {
            var k = k0
            var d = r
            while (d < 10) {
                while (cnt[d] > 0 && k > 0) {
                    cnt[d]--
                    k--
                }
                if (k == 0) return true
                d += 3
            }
            return false
        }
        if (rem != 0 && !remove(rem, 1)) remove(3 - rem, 2)
        val sb = StringBuilder()
        for (d in 9 downTo 0) {
            repeat(cnt[d]) { sb.append(d) }
        }
        val s = sb.toString()
        return if (s.isNotEmpty() && s[0] == '0') "0" else s
    }
}
