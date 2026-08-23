// LeetCode 0414 - Third Maximum Number

// https://leetcode.com/problems/third-maximum-number/



public class Solution {

    public int ThirdMax(int[] nums) {

        int? first = null;

        int? second = null;

        int? third = null;



        foreach (int value in nums) {

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



        return third ?? first!.Value;

    }

}
