// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

public class Solution {
    public int NumberOfSpecialSubstrings(string s) {
        int n = s.Length, ans = 0, left = 0;
        int[] cnt = new int[26];
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'a';
            cnt[c]++;
            while (cnt[c] > 1) { cnt[s[left] - 'a']--; left++; }
            ans += i - left + 1;
        }
        return ans;
    }
}
