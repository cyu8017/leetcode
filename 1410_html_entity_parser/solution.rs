// LeetCode 1410 - HTML Entity Parser
// https://leetcode.com/problems/html-entity-parser/

impl Solution {
    pub fn entity_parser(mut text: String) -> String {
        // Replace &amp; last so intermediate ampersands are not re-decoded.
        let entities = [
            ("&quot;", "\""),
            ("&apos;", "'"),
            ("&gt;", ">"),
            ("&lt;", "<"),
            ("&frasl;", "/"),
            ("&amp;", "&"),
        ];
        for (encoded, decoded) in entities {
            text = text.replace(encoded, decoded);
        }
        text
    }
}
