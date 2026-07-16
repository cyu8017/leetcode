// LeetCode 0055 - Jump Game
// https://leetcode.com/problems/jump-game/

public class Solution {
    public bool CanJump(int[] nums) {
        int farthest = 0;

        for (int i = 0; i < nums.Length; i++) {
            if (i > farthest) {
                return false;
            }
            farthest = Math.Max(farthest, i + nums[i]);
        }

        return true;
    }
}
