// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

import java.util.Arrays;

class Solution {
    public int countElements(int[] nums, int k) {
        int n = nums.length;
        if (k == 0) return n;
        Arrays.sort(nums);
        int ans = 0;
        for (int i = 0; i < n - k; i++) {
            if (nums[n - k] > nums[i]) ans++;
        }
        return ans;
    }
}
