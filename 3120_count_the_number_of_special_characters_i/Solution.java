// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution {
    public int numberOfSpecialChars(String word) {
        boolean[] s = new boolean[128];
        for (int i = 0; i < word.length(); i++) s[word.charAt(i)] = true;
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (s['a' + i] && s['A' + i]) ans++;
        }
        return ans;
    }
}
