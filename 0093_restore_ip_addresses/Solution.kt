// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

class Solution {
    fun restoreIpAddresses(s: String): List<String> {
        val result = mutableListOf<String>()
        val path = mutableListOf<String>()

        fun backtrack(start: Int) {
            if (path.size == 4) {
                if (start == s.length) {
                    result.add(path.joinToString("."))
                }
                return
            }

            for (length in 1..3) {
                if (start + length > s.length) {
                    break
                }
                val part = s.substring(start, start + length)
                if ((part.startsWith("0") && part.length > 1) || part.toInt() > 255) {
                    continue
                }
                path.add(part)
                backtrack(start + length)
                path.removeAt(path.size - 1)
            }
        }

        backtrack(0)
        return result
    }
}
