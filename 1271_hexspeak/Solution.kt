// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

import java.math.BigInteger

class Solution {
    fun toHexspeak(num: String): String {
        var value = BigInteger(num)
        val digits = "0123456789ABCDEF"
        val out = StringBuilder()
        while (value.signum() > 0) {
            val rem = value.mod(BigInteger.valueOf(16)).toInt()
            if (rem in 2..9) return "ERROR"
            out.insert(0, digits[rem])
            value = value.divide(BigInteger.valueOf(16))
        }
        val result = if (out.isEmpty()) "0" else out.toString()
        return result.replace('0', 'O').replace('1', 'I')
    }
}
