// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

class Solution {
    fun validIPAddress(queryIP: String): String {
        return when {
            isIpv4(queryIP) -> "IPv4"
            isIpv6(queryIP) -> "IPv6"
            else -> "Neither"
        }
    }

    private fun isIpv4(address: String): Boolean {
        val parts = address.split('.')
        if (parts.size != 4) {
            return false
        }
        for (part in parts) {
            if (!part.all { it.isDigit() } || part.length > 1 && part[0] == '0') {
                return false
            }
            if (part.isEmpty() || part.length > 3) {
                return false
            }
            val value = part.toInt()
            if (value > 255) {
                return false
            }
        }
        return true
    }

    private fun isIpv6(address: String): Boolean {
        val parts = address.split(':')
        if (parts.size != 8) {
            return false
        }
        for (part in parts) {
            if (part.isEmpty() || part.length > 4) {
                return false
            }
            if (!part.all { it.isDigit() || it in 'a'..'f' || it in 'A'..'F' }) {
                return false
            }
        }
        return true
    }
}
