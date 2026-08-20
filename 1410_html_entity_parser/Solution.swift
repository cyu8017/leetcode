// LeetCode 1410 - HTML Entity Parser
// https://leetcode.com/problems/html-entity-parser/

class Solution {
    func entityParser(_ text: String) -> String {
        var text = text
        let pairs = [("&quot;", "\""), ("&apos;", "'"), ("&gt;", ">"), ("&lt;", "<"), ("&frasl;", "/"), ("&amp;", "&")]
        for (enc, dec) in pairs {
            text = text.replacingOccurrences(of: enc, with: dec)
        }
        return text
    }
}
