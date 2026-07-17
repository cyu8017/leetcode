// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

import java.util.Arrays;

class Solution {
    public int reinitializePermutation(int n) {
        int[] perm = new int[n];
        for (int i = 0; i < n; i++) {
            perm[i] = i;
        }
        int[] target = perm.clone();
        int operations = 0;

        while (true) {
            int[] newPerm = new int[n];
            for (int i = 0; i < n; i++) {
                if (i % 2 == 0) {
                    newPerm[i] = perm[i / 2];
                } else {
                    newPerm[i] = perm[n / 2 + (i - 1) / 2];
                }
            }
            perm = newPerm;
            operations++;
            if (Arrays.equals(perm, target)) {
                return operations;
            }
        }
    }
}
