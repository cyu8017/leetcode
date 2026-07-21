// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

public class Solution {
    public int ReinitializePermutation(int n) {
        int[] perm = new int[n];
        int[] target = new int[n];
        for (int i = 0; i < n; i++) {
            perm[i] = i;
            target[i] = i;
        }
        int operations = 0;
        while (true) {
            int[] next = new int[n];
            for (int i = 0; i < n; i++) {
                next[i] = i % 2 == 0 ? perm[i / 2] : perm[n / 2 + (i - 1) / 2];
            }
            perm = next;
            operations++;
            bool same = true;
            for (int i = 0; i < n; i++) {
                if (perm[i] != target[i]) { same = false; break; }
            }
            if (same) return operations;
        }
    }
}
