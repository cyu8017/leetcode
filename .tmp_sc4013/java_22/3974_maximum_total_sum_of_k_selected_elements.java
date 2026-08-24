// CONFIG class=Solution method=maxSum types=None
// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

import java.util.Arrays;

class Solution {
    public long maxSum(int[] nums, int k, int mul) {
        Arrays.sort(nums);
        int n = nums.length;
        long ans = 0;
        for (int i = n - 1; i >= n - k; i--) {
            int m = Math.max(1, mul);
            ans += (long)nums[i] * m;
            mul--;
        }
        return ans;
    }
}
