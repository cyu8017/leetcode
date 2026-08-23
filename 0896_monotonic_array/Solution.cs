// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

public class Solution {
    public bool IsMonotonic(int[] nums) {
        bool inc = true, dec = true;
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] < nums[i - 1]) inc = false;
            if (nums[i] > nums[i - 1]) dec = false;
        }
        return inc || dec;
    }
}
