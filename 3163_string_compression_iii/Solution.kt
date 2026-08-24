// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

class Solution {
    fun compressedString(word: String): String {
        var ans = StringBuilder()
        var n = word.length
        var i = 0
        while (i < n) {
            var j = i + 1
            while (j < n && word[j] == word[i]) j++
            var k = j - i
            while (k > 0) {
                var x = minOf(9, k)
                ans.append((char)('0' + x))
                ans.append(word[i])
                k -= x
            }
            i = j
            
        }
        return ans.toString()
    }
}
