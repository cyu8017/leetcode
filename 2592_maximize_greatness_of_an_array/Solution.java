// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

import java.util.Arrays;

class Solution {
    public int maximizeGreatness(int[] nums) {
        Arrays.sort(nums);
        int i = 0;
        for (int x : nums) {
            if (x > nums[i]) i++;
        }
        return i;
    }
}
