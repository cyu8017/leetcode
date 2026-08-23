// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution {
    public int minSteps(String s, String t) {
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) freq[s.charAt(i) - 'a']++;
        for (int i = 0; i < t.length(); i++) freq[t.charAt(i) - 'a']--;
        int ans = 0;
        for (int v : freq) ans += Math.abs(v);
        return ans;
    }
}
