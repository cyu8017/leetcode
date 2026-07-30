// LeetCode 1410 - Html Entity Parser
// https://leetcode.com/problems/html-entity-parser/

public class Solution {
    public string EntityParser(string text) {
        // amp last would break; process amp first carefully - use ordered replace like py (amp mid)
        text = text.Replace("&quot;", """);
        text = text.Replace("&apos;", "'");
        text = text.Replace("&gt;", ">");
        text = text.Replace("&lt;", "<");
        text = text.Replace("&frasl;", "/");
        text = text.Replace("&amp;", "&");
        return text;
    }
}
