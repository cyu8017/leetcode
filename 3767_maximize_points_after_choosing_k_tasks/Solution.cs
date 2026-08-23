// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

using System;

public class Solution {
    public long MaxPoints(int[] technique1, int[] technique2, int k) {
        int n = technique1.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (i, j) => (technique1[j] - technique2[j]).CompareTo(technique1[i] - technique2[i]));
        long ans = 0;
        foreach (int x in technique2) ans += x;
        for (int i = 0; i < k; i++) {
            int index = idx[i];
            ans -= technique2[index];
            ans += technique1[index];
        }
        for (int i = k; i < n; i++) {
            int index = idx[i];
            if (technique1[index] >= technique2[index]) {
                ans -= technique2[index];
                ans += technique1[index];
            }
        }
        return ans;
    }
}
