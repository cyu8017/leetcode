// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution {
    public int countLetters(String s) {
        int ans = 1, length = 1;
        for (int i = 1; i < s.length(); i++) {
            length = s.charAt(i) == s.charAt(i - 1) ? length + 1 : 1;
            ans += length;
        }
        return ans;
    }
}
