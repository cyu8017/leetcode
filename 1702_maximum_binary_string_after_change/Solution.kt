// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

class Solution {
    fun maximumBinaryString(binary: String): String {
        val zeros = binary.count { it == '0' }
        if (zeros <= 1) {
            return binary
        }
        val first = binary.indexOf('0')
        val n = binary.length
        return "1".repeat(first + zeros - 1) + "0" + "1".repeat(n - first - zeros)
    }
}
