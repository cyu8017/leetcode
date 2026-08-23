// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

import java.util.Arrays;

class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        long ans = 0;
        for (int i = 0; i < k; i++) {
            int x = happiness[happiness.length - i - 1] - i;
            ans += Math.max(x, 0);
        }
        return ans;
    }
}
