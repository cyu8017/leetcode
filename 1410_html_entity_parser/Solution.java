// LeetCode 1410 - Html Entity Parser
// https://leetcode.com/problems/html-entity-parser/

class Solution {
    public String entityParser(String text) {
        // amp last would break; process amp first carefully - use ordered replace like py (amp mid)
        text = text.replace("&quot;", """);
        text = text.replace("&apos;", "'");
        text = text.replace("&gt;", ">");
        text = text.replace("&lt;", "<");
        text = text.replace("&frasl;", "/");
        text = text.replace("&amp;", "&");
        return text;
    }
}
