// LeetCode 1410 - HTML Entity Parser
// https://leetcode.com/problems/html-entity-parser/

class Solution {
    fun entityParser(text: String): String {
        var result = text
        result = result.replace("&quot;", "\"")
        result = result.replace("&apos;", "'")
        result = result.replace("&gt;", ">")
        result = result.replace("&lt;", "<")
        result = result.replace("&frasl;", "/")
        result = result.replace("&amp;", "&")
        return result
    }
}
