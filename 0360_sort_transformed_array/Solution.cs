// LeetCode 0360 - Sort Transformed Array

// https://leetcode.com/problems/sort-transformed-array/



public class Solution {

    public int[] SortTransformedArray(int[] nums, int a, int b, int c) {

        int left = 0;

        int right = nums.Length - 1;

        int[] result = new int[nums.Length];

        int index = a > 0 ? nums.Length - 1 : 0;

        int step = a > 0 ? -1 : 1;



        while (left <= right) {

            int leftValue = Transform(nums[left], a, b, c);

            int rightValue = Transform(nums[right], a, b, c);



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



    private int Transform(int value, int a, int b, int c) {

        return a * value * value + b * value + c;

    }

}
