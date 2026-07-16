// LeetCode 0376 - Wiggle Subsequence

// https://leetcode.com/problems/wiggle-subsequence/



public class Solution {

    public int WiggleMaxLength(int[] nums) {

        if (nums.Length < 2) {

            return nums.Length;

        }



        int up = 1;

        int down = 1;



        for (int index = 1; index < nums.Length; index++) {

            if (nums[index] > nums[index - 1]) {

                up = down + 1;

            } else if (nums[index] < nums[index - 1]) {

                down = up + 1;

            }

        }



        return System.Math.Max(up, down);

    }

}
