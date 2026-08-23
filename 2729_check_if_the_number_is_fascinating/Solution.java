// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

class Solution {
    public boolean isFascinating(int n) {
        String s = Integer.toString(n) + Integer.toString(2 * n) + Integer.toString(3 * n);
        if (s.length() != 9) return false;
        int[] cnt = new int[10];
        for (char c : s.toCharArray()) cnt[c - '0']++;
        if (cnt[0] != 0) return false;
        for (int i = 1; i <= 9; i++) if (cnt[i] != 1) return false;
        return true;
    }
}
