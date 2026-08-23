// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

import java.util.*;

class Solution {
    public int maxWidthRamp(int[] nums) {
        List<Integer> stack = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (stack.isEmpty() || nums[stack.get(stack.size() - 1)] > nums[i]) stack.add(i);
        }
        int ans = 0;
        for (int j = nums.length - 1; j >= 0; j--) {
            while (!stack.isEmpty() && nums[stack.get(stack.size() - 1)] <= nums[j]) {
                ans = Math.max(ans, j - stack.get(stack.size() - 1));
                stack.remove(stack.size() - 1);
            }
        }
        return ans;
    }
}
