// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

class Solution {
    public int numberOfSpecialSubstrings(String s) {
        int n = s.length(), ans = 0, left = 0;
        int[] cnt = new int[26];
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            cnt[c]++;
            while (cnt[c] > 1) { cnt[s.charAt(left) - 'a']--; left++; }
            ans += i - left + 1;
        }
        return ans;
    }
}
