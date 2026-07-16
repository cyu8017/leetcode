// LeetCode 0330 - Patching Array

// https://leetcode.com/problems/patching-array/



class Solution {

    public int minPatches(int[] nums, int n) {

        int patches = 0;

        long miss = 1;

        int index = 0;

        while (miss <= n) {

            if (index < nums.length && nums[index] <= miss) {

                miss += nums[index];

                index++;

            } else {

                miss += miss;

                patches++;

            }

        }

        return patches;

    }

}

