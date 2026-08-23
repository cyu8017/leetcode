// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

import java.util.Arrays;

class Solution {
    public int[] numberGame(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i + 1 < nums.length; i += 2) {
            int t = nums[i];
            nums[i] = nums[i + 1];
            nums[i + 1] = t;
        }
        return nums;
    }
}
