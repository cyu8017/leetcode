// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

import java.util.Arrays;

class Solution {
    public int maxDistinctElements(int[] nums, int k) {
        Arrays.sort(nums);
        int ans = 0;
        long prev = Long.MIN_VALUE / 2;
        for (int x : nums) {
            long cur = x - k;
            if (cur <= prev) cur = prev + 1;
            if (cur > x + k) continue;
            ans++;
            prev = cur;
        }
        return ans;
    }
}
