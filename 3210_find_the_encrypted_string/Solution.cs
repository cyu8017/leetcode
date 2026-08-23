// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

public class Solution {
    public string GetEncryptedString(string s, int k) {
        int n = s.Length;
        char[] cs = new char[n];
        for (int i = 0; i < n; i++) cs[i] = s[(i + k) % n];
        return new string(cs);
    }
}
