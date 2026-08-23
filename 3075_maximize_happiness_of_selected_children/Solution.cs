// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

using System;

public class Solution {
    public long MaximumHappinessSum(int[] happiness, int k) {
        Array.Sort(happiness);
        long ans = 0;
        for (int i = 0; i < k; i++) {
            int x = happiness[happiness.Length - i - 1] - i;
            ans += Math.Max(x, 0);
        }
        return ans;
    }
}
