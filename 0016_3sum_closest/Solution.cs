// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        Array.Sort(nums);
        int closest = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.Length - 2; i++) {
            int left = i + 1;
            int right = nums.Length - 1;
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                if (Math.Abs(total - target) < Math.Abs(closest - target)) {
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
