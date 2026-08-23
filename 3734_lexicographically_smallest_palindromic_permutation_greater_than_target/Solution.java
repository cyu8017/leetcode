// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically_smallest_palindromic_permutation_greater_than_target/

class Solution {
    private int[] half;
    private char[] left;
    private String target;
    private int halfLen, mid;

    public String lexPalindromicPermutation(String s, String target) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        int odd = 0;
        mid = -1;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] % 2 == 1) { odd++; mid = i; }
        }
        if (odd > 1) return "";
        half = new int[26];
        for (int i = 0; i < 26; i++) half[i] = cnt[i] / 2;
        int n = s.length();
        halfLen = n / 2;
        this.target = target;
        left = new char[halfLen];
        if (!dfs(0, false)) return "";
        StringBuilder res = new StringBuilder();
        res.append(left);
        if (mid >= 0) res.append((char) ('a' + mid));
        for (int i = halfLen - 1; i >= 0; i--) res.append(left[i]);
        String out = res.toString();
        if (out.compareTo(target) <= 0) return "";
        return out;
    }

    private boolean dfs(int pos, boolean greater) {
        if (pos == halfLen) {
            if (mid >= 0) {
                if (greater) return true;
                return (char) ('a' + mid) > target.charAt(halfLen);
            }
            return greater;
        }
        int start = greater ? 0 : (target.charAt(pos) - 'a');
        for (int c = start; c < 26; c++) {
            if (half[c] == 0) continue;
            half[c]--;
            left[pos] = (char) ('a' + c);
            if (dfs(pos + 1, greater || c > (target.charAt(pos) - 'a'))) return true;
            half[c]++;
        }
        return false;
    }
}
