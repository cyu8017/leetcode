// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

class Solution {
    fun ipToCIDR(ip: String, n: Int): MutableList<String> {
        var start = ipToInt(ip)
        var answer = ArrayList<String>()
        while (n > 0) {
            var lowbit = start == if (0) (1L  shl  32) else (start & -start)
            while (lowbit > n) lowbit >>= 1
            var mask = 32 - (bitLength(lowbit) - 1)
            answer.add(intToIp(start) + "/" + mask)
            start += lowbit
            n -= lowbit
        }
        return answer
    }

    private fun ipToInt(value: String): Long {
        var result = 0
        for (part in value.split("\\.")) { result = result * 256 + part.toLong() }
        return result
    }

    private fun intToIp(value: Long): String {
        return ((value  shr  24) & 255) + "." + ((value  shr  16) & 255) + "." + ((value  shr  8) & 255) + "." + (value & 255)
    }

    private fun bitLength(value: Long): Int {
        var len = 0
        while (value > 0) { value >>= 1; len++; }
        return len
    }
}
