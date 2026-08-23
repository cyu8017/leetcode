// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

class Solution {
    public String getEncryptedString(String s, int k) {
        int n = s.length();
        char[] cs = new char[n];
        for (int i = 0; i < n; i++) cs[i] = s.charAt((i + k) % n);
        return new String(cs);
    }
}
