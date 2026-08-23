// LeetCode 0396 - Rotate Function

// https://leetcode.com/problems/rotate-function/



class Solution {

    public int maxRotateFunction(int[] nums) {

        int total = 0;

        int current = 0;



        for (int index = 0; index < nums.length; index++) {

            total += nums[index];

            current += index * nums[index];

        }



        int best = current;



        for (int index = nums.length - 1; index > 0; index--) {

            current += total - nums.length * nums[index];

            best = Math.max(best, current);

        }



        return best;

    }

}
