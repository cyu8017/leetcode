// LeetCode 0376 - Wiggle Subsequence

// https://leetcode.com/problems/wiggle-subsequence/



class Solution {

    public int wiggleMaxLength(int[] nums) {

        if (nums.length < 2) {

            return nums.length;

        }



        int up = 1;

        int down = 1;



        for (int index = 1; index < nums.length; index++) {

            if (nums[index] > nums[index - 1]) {

                up = down + 1;

            } else if (nums[index] < nums[index - 1]) {

                down = up + 1;

            }

        }



        return Math.max(up, down);

    }

}
