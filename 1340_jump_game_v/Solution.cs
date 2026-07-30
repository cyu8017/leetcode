// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

using System.Linq;
public class Solution {
    public int MaxJumps(int[] arr, int d) {
        int n = arr.Length;
        var dp = Enumerable.Repeat(1, n).ToArray();
        foreach (int i in Enumerable.Range(0, n).OrderBy(i => arr[i])) {
            foreach (int step in new[] { -1, 1 }) {
                int j = i + step;
                while (j >= 0 && j < n && System.Math.Abs(j - i) <= d && arr[j] < arr[i]) {
                    dp[i] = System.Math.Max(dp[i], 1 + dp[j]);
                    j += step;
                }
            }
        }
        return dp.Max();
    }
}
