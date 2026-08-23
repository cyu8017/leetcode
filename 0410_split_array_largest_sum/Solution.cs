// LeetCode 0410 - Split Array Largest Sum

// https://leetcode.com/problems/split-array-largest-sum/



public class Solution {

    public int SplitArray(int[] nums, int k) {

        int left = 0;

        int right = 0;



        foreach (int value in nums) {

            left = int.Max(left, value);

            right += value;

        }



        while (left < right) {

            int mid = left + (right - left) / 2;



            if (CanSplit(nums, k, mid)) {

                right = mid;

            } else {

                left = mid + 1;

            }

        }



        return left;

    }



    private static bool CanSplit(int[] nums, int k, int limit) {

        int parts = 1;

        int current = 0;



        foreach (int value in nums) {

            if (current + value > limit) {

                parts++;

                current = 0;

            }

            current += value;

        }



        return parts <= k;

    }

}
