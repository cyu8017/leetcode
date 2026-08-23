// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

public class Solution {
    public int MinOperations(int[] nums) {
        foreach (int x in nums) if (x != nums[0]) return 1;
        return 0;
    }
}
