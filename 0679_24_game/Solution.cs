// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

using System.Collections.Generic;

public class Solution {
    private const double Eps = 1e-6;

    public bool JudgePoint24(int[] cards) {
        var nums = new List<double>();
        foreach (int card in cards) nums.Add(card);
        return Dfs(nums);
    }

    private bool Dfs(List<double> nums) {
        if (nums.Count == 1) return System.Math.Abs(nums[0] - 24.0) < Eps;
        for (int i = 0; i < nums.Count; ++i) {
            for (int j = 0; j < nums.Count; ++j) {
                if (i == j) continue;
                var rest = new List<double>();
                for (int k = 0; k < nums.Count; ++k) {
                    if (k != i && k != j) rest.Add(nums[k]);
                }
                double a = nums[i], b = nums[j];
                var candidates = new List<double> { a + b, a - b, a * b };
                if (System.Math.Abs(b) > Eps) candidates.Add(a / b);
                foreach (double value in candidates) {
                    rest.Add(value);
                    if (Dfs(rest)) return true;
                    rest.RemoveAt(rest.Count - 1);
                }
            }
        }
        return false;
    }
}
