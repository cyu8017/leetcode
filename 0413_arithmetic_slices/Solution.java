// LeetCode 0413 - Arithmetic Slices

// https://leetcode.com/problems/arithmetic-slices/



class Solution {

    public int numberOfArithmeticSlices(int[] nums) {

        if (nums.length < 3) {

            return 0;

        }



        int total = 0;

        int current = 0;



        for (int index = 2; index < nums.length; index++) {

            if (nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]) {

                current++;

                total += current;

            } else {

                current = 0;

            }

        }



        return total;

    }

}
