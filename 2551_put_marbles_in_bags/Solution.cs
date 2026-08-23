// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

using System;

public class Solution {
    public long PutMarbles(int[] weights, int k) {
        int n = weights.Length;
        if (k == 1 || k == n) return 0;
        int[] pair = new int[n - 1];
        for (int i = 0; i < n - 1; ++i) pair[i] = weights[i] + weights[i + 1];
        Array.Sort(pair);
        long mn = 0, mx = 0;
        for (int i = 0; i < k - 1; ++i) {
            mn += pair[i];
            mx += pair[n - 2 - i];
        }
        return mx - mn;
    }
}
