// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

public class Solution {
    public int[] FindErrorNums(int[] nums) {
        int n = nums.Length;
        int[] seen = new int[n + 1];
        int duplicate = -1, missing = -1;
        foreach (int value in nums) ++seen[value];
        for (int value = 1; value <= n; ++value) {
            if (seen[value] == 2) duplicate = value;
            else if (seen[value] == 0) missing = value;
        }
        return new[] { duplicate, missing };
    }
}
