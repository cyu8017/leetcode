// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

class Solution {
    public int minMaxGame(int[] nums) {
        while (nums.length > 1) {
            int[] next = new int[nums.length / 2];
            for (int i = 0; i < next.length; i++) {
                if (i % 2 == 0) next[i] = Math.min(nums[2 * i], nums[2 * i + 1]);
                else next[i] = Math.max(nums[2 * i], nums[2 * i + 1]);
            }
            nums = next;
        }
        return nums[0];
    }
}
