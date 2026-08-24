// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

class Solution {
    fun betterCompression(compressed: String): String {
        var cnt = IntArray(26)
        var n = compressed.length
        var i = 0
        while (i < n) {
            var c = compressed[i]
            var j = i + 1
            var x = 0
            while (j < n) {
                var d = compressed[j]
                if (d < '0' || d > '9') break
                x = x * 10 + (d - '0')
                j++
            }
            cnt[c - 'a'] += x
            i = j
            
        }
        var ans = StringBuilder()
        for (char c = 'a'; c <= 'z'; c++) {
            if (cnt[c - 'a'] > 0) {
                ans.append(c)
                ans.append(cnt[c - 'a'])
            }
        }
        return ans.toString()
    }
}
