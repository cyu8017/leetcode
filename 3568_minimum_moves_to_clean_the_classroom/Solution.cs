// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

using System.Collections.Generic;

public class Solution {
    public int MinMoves(string[] classroom, int energy) {
        int m = classroom.Length, n = classroom[0].Length;
        int[][] d = new int[m][];
        for (int i = 0; i < m; i++) d[i] = new int[n];
        int x = 0, y = 0, cnt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = classroom[i][j];
                if (c == 'S') { x = i; y = j; }
                else if (c == 'L') d[i][j] = cnt++;
            }
        }
        if (cnt == 0) return 0;

        bool[][][][] vis = new bool[m][][][];
        for (int i = 0; i < m; i++) {
            vis[i] = new bool[n][][];
            for (int j = 0; j < n; j++) {
                vis[i][j] = new bool[energy + 1][];
                for (int e = 0; e <= energy; e++) vis[i][j][e] = new bool[1 << cnt];
            }
        }
        var q = new List<(int i, int j, int curEnergy, int mask)> { (x, y, energy, (1 << cnt) - 1) };
        vis[x][y][energy][(1 << cnt) - 1] = true;
        int[] dirs = { -1, 0, 1, 0, -1 };
        int ans = 0;
        while (q.Count > 0) {
            var t = q;
            q = new List<(int, int, int, int)>();
            foreach (var s in t) {
                int i = s.i, j = s.j, curEnergy = s.curEnergy, mask = s.mask;
                if (mask == 0) return ans;
                if (curEnergy <= 0) continue;
                for (int kk = 0; kk < 4; kk++) {
                    int nx = i + dirs[kk], ny = j + dirs[kk + 1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && classroom[nx][ny] != 'X') {
                        int nxtEnergy = classroom[nx][ny] == 'R' ? energy : curEnergy - 1;
                        int nxtMask = mask;
                        if (classroom[nx][ny] == 'L') nxtMask &= ~(1 << d[nx][ny]);
                        if (!vis[nx][ny][nxtEnergy][nxtMask]) {
                            vis[nx][ny][nxtEnergy][nxtMask] = true;
                            q.Add((nx, ny, nxtEnergy, nxtMask));
                        }
                    }
                }
            }
            ans++;
        }
        return -1;
    }
}
