// LeetCode 0324 - Wiggle Sort II

// https://leetcode.com/problems/wiggle-sort-ii/



import java.util.Arrays;



class Solution {

    public void wiggleSort(int[] nums) {

        int[] sortedNums = Arrays.copyOf(nums, nums.length);

        Arrays.sort(sortedNums);

        int left = (nums.length - 1) / 2;

        int right = nums.length - 1;

        for (int index = 0; index < nums.length; index++) {

            if (index % 2 == 0) {

                nums[index] = sortedNums[left];

                left--;

            } else {

                nums[index] = sortedNums[right];

                right--;

            }

        }

    }

}

