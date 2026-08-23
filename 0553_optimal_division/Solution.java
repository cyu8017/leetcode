// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

class Solution {
    public String optimalDivision(int[] nums) {
        if (nums.length == 1) {
            return String.valueOf(nums[0]);
        }
        if (nums.length == 2) {
            return nums[0] + "/" + nums[1];
        }

        StringBuilder result = new StringBuilder();
        result.append(nums[0]).append("/(");
        for (int i = 1; i < nums.length; ++i) {
            if (i > 1) {
                result.append('/');
            }
            result.append(nums[i]);
        }
        result.append(')');
        return result.toString();
    }
}
