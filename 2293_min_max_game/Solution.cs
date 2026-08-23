// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

using System;

public class Solution {
    public int MinMaxGame(int[] nums) {
        while (nums.Length > 1) {
            int[] next = new int[nums.Length / 2];
            for (int i = 0; i < next.Length; i++) {
                if (i % 2 == 0) next[i] = Math.Min(nums[2 * i], nums[2 * i + 1]);
                else next[i] = Math.Max(nums[2 * i], nums[2 * i + 1]);
            }
            nums = next;
        }
        return nums[0];
    }
}
