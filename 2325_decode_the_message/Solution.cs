// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

public class Solution {
    public string DecodeMessage(string key, string message) {
        char[] mp = new char[26];
        char next = 'a';
        foreach (char c in key) {
            if (c == ' ' || mp[c - 'a'] != 0) continue;
            mp[c - 'a'] = next++;
        }
        char[] outc = message.ToCharArray();
        for (int i = 0; i < outc.Length; i++) {
            if (outc[i] != ' ') outc[i] = mp[outc[i] - 'a'];
        }
        return new string(outc);
    }
}
