// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

public class Solution {
    public int[] FindThePrefixCommonArray(int[] A, int[] B) {
        int n = A.Length;
        bool[] seenA = new bool[n + 1], seenB = new bool[n + 1];
        int[] ans = new int[n];
        int common = 0;
        for (int i = 0; i < n; i++) {
            if (seenB[A[i]]) common++;
            seenA[A[i]] = true;
            if (seenA[B[i]]) common++;
            seenB[B[i]] = true;
            ans[i] = common;
        }
        return ans;
    }
}
