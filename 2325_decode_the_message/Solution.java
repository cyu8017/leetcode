// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

class Solution {
    public String decodeMessage(String key, String message) {
        char[] mp = new char[26];
        char next = 'a';
        for (char c : key) {
            if (c == ' ' || mp[c - 'a'] != 0) continue;
            mp[c - 'a'] = next++;
        }
        char[] outc = message.toCharArray();
        for (int i = 0; i < outc.length; i++) {
            if (outc[i] != ' ') outc[i] = mp[outc[i] - 'a'];
        }
        return new String(outc);
    }
}
