// LeetCode 0414 - Third Maximum Number

// https://leetcode.com/problems/third-maximum-number/



class Solution {

    public int thirdMax(int[] nums) {

        Integer first = null;

        Integer second = null;

        Integer third = null;



        for (int value : nums) {

            if (value == first || value == second || value == third) {

                continue;

            }



            if (first == null || value > first) {

                third = second;

                second = first;

                first = value;

            } else if (second == null || value > second) {

                third = second;

                second = value;

            } else if (third == null || value > third) {

                third = value;

            }

        }



        return third != null ? third : first;

    }

}
