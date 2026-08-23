// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

class Solution {
    public boolean isGood(int[] nums) {
        int n = nums.length - 1;
        if (n < 1) return false;
        int[] freq = new int[n + 1];
        for (int v : nums) {
            if (v < 1 || v > n) return false;
            freq[v]++;
        }
        for (int i = 1; i < n; i++) if (freq[i] != 1) return false;
        return freq[n] == 2;
    }
}
