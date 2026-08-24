// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

class Solution {
    fun f(x0: Int, k: Int): String {
        var x = x0
        val res = StringBuilder()
        while (x > 0) {
            val v = x % k
            res.append(if (v <= 9) ('0'.code + v).toChar() else ('A'.code + v - 10).toChar())
            x /= k
        }
        return res.reverse().toString()
    }

    fun concatHex36(n: Int): String {
        return f(n * n, 16) + f(n * n * n, 36)
    }
}
