// LeetCode 0324 - Wiggle Sort II

// https://leetcode.com/problems/wiggle-sort-ii/



using System.Linq;



public class Solution {

    public void WiggleSort(int[] nums) {

        int[] sortedNums = nums.OrderBy(value => value).ToArray();

        int left = (nums.Length - 1) / 2;

        int right = nums.Length - 1;

        for (int index = 0; index < nums.Length; index++) {

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

