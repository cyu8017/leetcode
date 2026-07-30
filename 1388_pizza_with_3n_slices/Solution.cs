// LeetCode 1388 - Pizza With 3n Slices
// https://leetcode.com/problems/pizza-with-3n-slices/

public class Solution {
    public int MaxSizeSlices(int[] slices) {
        int k = slices.Length / 3;
        int Line(int[] a) {
            var dp = new int[a.Length + 2, k + 1];
            for (int i = 0; i < a.Length; i++)
                for (int j = 1; j <= k; j++)
                    dp[i + 2, j] = System.Math.Max(dp[i + 1, j], dp[i, j - 1] + a[i]);
            return dp[a.Length + 1, k];
        }
        var left = new int[slices.Length - 1];
        var right = new int[slices.Length - 1];
        System.Array.Copy(slices, 0, left, 0, slices.Length - 1);
        System.Array.Copy(slices, 1, right, 0, slices.Length - 1);
        return System.Math.Max(Line(left), Line(right));
    }
}
