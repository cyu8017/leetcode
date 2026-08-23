// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closest = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                if (Math.abs(total - target) < Math.abs(closest - target)) {
                    closest = total;
                }
                if (total < target) {
                    left++;
                } else if (total > target) {
                    right--;
                } else {
                    return total;
                }
            }
        }

        return closest;
    }
}
