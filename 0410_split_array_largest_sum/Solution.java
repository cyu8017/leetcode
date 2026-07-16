// LeetCode 0410 - Split Array Largest Sum

// https://leetcode.com/problems/split-array-largest-sum/



class Solution {

    public int splitArray(int[] nums, int k) {

        int left = 0;

        int right = 0;



        for (int value : nums) {

            left = Math.max(left, value);

            right += value;

        }



        while (left < right) {

            int mid = left + (right - left) / 2;



            if (canSplit(nums, k, mid)) {

                right = mid;

            } else {

                left = mid + 1;

            }

        }



        return left;

    }



    private boolean canSplit(int[] nums, int k, int limit) {

        int parts = 1;

        int current = 0;



        for (int value : nums) {

            if (current + value > limit) {

                parts++;

                current = 0;

            }

            current += value;

        }



        return parts <= k;

    }

}
