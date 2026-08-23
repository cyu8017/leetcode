// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

import java.util.Arrays;

class Solution {
    public int maxNumOfMarkedIndices(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int i = 0, ans = 0;
        for (int j = (n + 1) / 2; j < n; ++j) {
            if (2 * nums[i] <= nums[j]) {
                ans += 2;
                i++;
            }
        }
        return ans;
    }
}
