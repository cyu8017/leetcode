// LeetCode 0330 - Patching Array

// https://leetcode.com/problems/patching-array/



public class Solution {

    public int MinPatches(int[] nums, int n) {

        int patches = 0;

        long miss = 1;

        int index = 0;

        while (miss <= n) {

            if (index < nums.Length && nums[index] <= miss) {

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

