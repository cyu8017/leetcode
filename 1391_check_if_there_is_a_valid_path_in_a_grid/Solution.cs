// LeetCode 1391 - Check If There Is A Valid Path In A Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

using System.Collections.Generic;
public class Solution {
    public bool HasValidPath(int[][] grid) {
        var dirs = new Dictionary<int, (int,int)[]> {
            [1] = new[]{(0,-1),(0,1)}, [2] = new[]{(-1,0),(1,0)},
            [3] = new[]{(0,-1),(1,0)}, [4] = new[]{(0,1),(1,0)},
            [5] = new[]{(0,-1),(-1,0)}, [6] = new[]{(0,1),(-1,0)}
        };
        int m = grid.Length, n = grid[0].Length;
        var seen = new HashSet<(int,int)> { (0,0) };
        var st = new Stack<(int,int)>(); st.Push((0,0));
        while (st.Count > 0) {
            var (r, c) = st.Pop();
            if (r == m - 1 && c == n - 1) return true;
            foreach (var (dr, dc) in dirs[grid[r][c]]) {
                int x = r + dr, y = c + dc;
                if (x >= 0 && x < m && y >= 0 && y < n && !seen.Contains((x, y))) {
                    bool ok = false;
                    foreach (var (odr, odc) in dirs[grid[x][y]])
                        if (odr == -dr && odc == -dc) ok = true;
                    if (ok) { seen.Add((x, y)); st.Push((x, y)); }
                }
            }
        }
        return false;
    }
}
