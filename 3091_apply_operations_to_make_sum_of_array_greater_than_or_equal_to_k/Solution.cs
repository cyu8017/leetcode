// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

using System;

public class Solution {
    public int MinOperations(int k) {
        int ans = k;
        for (int a = 0; a < k; a++) {
            int x = a + 1;
            int b = (k + x - 1) / x - 1;
            ans = Math.Min(ans, a + b);
        }
        return ans;
    }
}
