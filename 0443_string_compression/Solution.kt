// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

class Solution {
    fun compress(chars: CharArray): Int {
        var write = 0
        var read = 0
        while (read < chars.size) {
            val ch = chars[read]
            var count = 0
            while (read < chars.size && chars[read] == ch) {
                read++
                count++
            }
            chars[write++] = ch
            if (count > 1) {
                for (digit in count.toString()) {
                    chars[write++] = digit
                }
            }
        }
        return write
    }
}
