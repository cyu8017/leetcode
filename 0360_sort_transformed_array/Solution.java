// LeetCode 0360 - Sort Transformed Array

// https://leetcode.com/problems/sort-transformed-array/



class Solution {

    public int[] sortTransformedArray(int[] nums, int a, int b, int c) {

        int left = 0;

        int right = nums.length - 1;

        int[] result = new int[nums.length];

        int index = a > 0 ? nums.length - 1 : 0;

        int step = a > 0 ? -1 : 1;



        while (left <= right) {

            int leftValue = transform(nums[left], a, b, c);

            int rightValue = transform(nums[right], a, b, c);



            if (a > 0) {

                if (leftValue > rightValue) {

                    result[index] = leftValue;

                    left++;

                } else {

                    result[index] = rightValue;

                    right--;

                }

            } else if (leftValue < rightValue) {

                result[index] = leftValue;

                left++;

            } else {

                result[index] = rightValue;

                right--;

            }



            index += step;

        }



        return result;

    }



    private int transform(int value, int a, int b, int c) {

        return a * value * value + b * value + c;

    }

}
