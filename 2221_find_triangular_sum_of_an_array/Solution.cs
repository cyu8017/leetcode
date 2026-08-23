// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

public class Solution {
    public int TriangularSum(int[] nums) {
        while (nums.Length > 1) {
            int[] next = new int[nums.Length - 1];
            for (int i = 0; i < next.Length; i++)
                next[i] = (nums[i] + nums[i + 1]) % 10;
            nums = next;
        }
        return nums[0];
    }
}
