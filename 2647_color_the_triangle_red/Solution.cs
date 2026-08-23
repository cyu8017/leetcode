// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

using System.Collections.Generic;

public class Solution {
    public int[][] ColorRed(int n) {
        var ans = new List<int[]>();
        for (int i = 1; i <= n; i++) ans.Add(new int[] { i, 1 });
        for (int i = n % 2 + 2; i <= n; i += 2)
            for (int j = 2; j <= 2 * (n - i) + 2; j++)
                ans.Add(new int[] { i, j });
        return ans.ToArray();
    }
}
