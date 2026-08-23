// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

using System.Text;

public class Solution {
    public string OptimalDivision(int[] nums) {
        if (nums.Length == 1) return nums[0].ToString();
        if (nums.Length == 2) return nums[0] + "/" + nums[1];
        var result = new StringBuilder();
        result.Append(nums[0]).Append("/(");
        for (int i = 1; i < nums.Length; ++i) {
            if (i > 1) result.Append('/');
            result.Append(nums[i]);
        }
        result.Append(')');
        return result.ToString();
    }
}
