using System;

public class Solution
{
    public int CalculateMinimumHP(int[][] dungeon)
    {
        var rows = dungeon.Length;
        var cols = dungeon[0].Length;
        var dp = new int[rows + 1, cols + 1];

        for (var r = 0; r <= rows; r++)
        {
            for (var c = 0; c <= cols; c++)
            {
                dp[r, c] = int.MaxValue;
            }
        }
        dp[rows, cols - 1] = 1;
        dp[rows - 1, cols] = 1;

        for (var r = rows - 1; r >= 0; r--)
        {
            for (var c = cols - 1; c >= 0; c--)
            {
                var needed = Math.Min(dp[r + 1, c], dp[r, c + 1]) - dungeon[r][c];
                dp[r, c] = Math.Max(1, needed);
            }
        }
        return dp[0, 0];
    }
}
