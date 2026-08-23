// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution {
    public int findPermutationDifference(String s, String t) {
        int[] d = new int[26];
        for (int i = 0; i < s.length(); i++) d[s.charAt(i) - 'a'] = i;
        int ans = 0;
        for (int i = 0; i < t.length(); i++) ans += Math.abs(d[t.charAt(i) - 'a'] - i);
        return ans;
    }
}
