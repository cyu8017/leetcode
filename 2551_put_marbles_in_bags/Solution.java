// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

import java.util.Arrays;

class Solution {
    public long putMarbles(int[] weights, int k) {
        int n = weights.length;
        if (k == 1 || k == n) return 0;
        int[] pair = new int[n - 1];
        for (int i = 0; i < n - 1; ++i) pair[i] = weights[i] + weights[i + 1];
        Arrays.sort(pair);
        long mn = 0, mx = 0;
        for (int i = 0; i < k - 1; ++i) {
            mn += pair[i];
            mx += pair[n - 2 - i];
        }
        return mx - mn;
    }
}
