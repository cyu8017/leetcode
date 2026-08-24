// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

class Solution {
    fun decodeMessage(key: String, message: String): String {
        val mp = CharArray(26)
        var next = 'a'
        for (c in key) {
            if (c == ' ' || mp[c - 'a'] != 0.toChar()) continue
            mp[c - 'a'] = next
            next++
        }
        val out = message.toCharArray()
        for (i in out.indices) {
            if (out[i] != ' ') out[i] = mp[out[i] - 'a']
        }
        return String(out)
    }
}
