// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

public class Solution {
    public int[] GetBiggestThree(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        var s1 = new int[m + 1][];
        var s2 = new int[m + 1][];
        for (int i = 0; i <= m; i++) {
            s1[i] = new int[n + 2];
            s2[i] = new int[n + 2];
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int value = grid[i - 1][j - 1];
                s1[i][j] = s1[i - 1][j - 1] + value;
                s2[i][j] = s2[i - 1][j + 1] + value;
            }
        }

        var rhombusSums = new HashSet<int>();
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int value = grid[i - 1][j - 1];
                int limit = Math.Min(Math.Min(i - 1, m - i), Math.Min(j - 1, n - j));
                rhombusSums.Add(value);
                for (int k = 1; k <= limit; k++) {
                    int a = s1[i + k][j] - s1[i][j - k];
                    int b = s1[i][j + k] - s1[i - k][j];
                    int c = s2[i][j - k] - s2[i - k][j];
                    int d = s2[i + k][j] - s2[i][j + k];
                    rhombusSums.Add(a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]);
                }
            }
        }

        var sorted = rhombusSums.ToArray();
        Array.Sort(sorted, (x, y) => y.CompareTo(x));
        int take = Math.Min(3, sorted.Length);
        var answer = new int[take];
        Array.Copy(sorted, answer, take);
        return answer;
    }
}
