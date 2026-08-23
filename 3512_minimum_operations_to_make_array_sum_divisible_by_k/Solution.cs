// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

public class Solution {
    public int MinOperations(int[] nums, int k) {
        int ans = 0;
        foreach (int x in nums) ans = (ans + x) % k;
        return ans;
    }
}
