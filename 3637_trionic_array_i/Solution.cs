// LeetCode 3637 - Trionic Array I
// https://leetcode.com/problems/trionic-array-i/

public class Solution {
    public bool IsTrionic(int[] nums) {
        int n = nums.Length, p = 0;
        while (p < n - 2 && nums[p] < nums[p + 1]) p++;
        if (p == 0) return false;
        int q = p;
        while (q < n - 1 && nums[q] > nums[q + 1]) q++;
        if (q == p || q == n - 1) return false;
        while (q < n - 1 && nums[q] < nums[q + 1]) q++;
        return q == n - 1;
    }
}
