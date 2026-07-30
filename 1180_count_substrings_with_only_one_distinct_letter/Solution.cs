// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

public class Solution {
    public int CountLetters(string s) {
        int ans = 1, length = 1;
        for (int i = 1; i < s.Length; i++) {
            length = s[i] == s[i - 1] ? length + 1 : 1;
            ans += length;
        }
        return ans;
    }
}
