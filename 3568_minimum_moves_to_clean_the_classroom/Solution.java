// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length, n = classroom[0].length();
        int[][] d = new int[m][n];
        int x = 0, y = 0, cnt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = classroom[i].charAt(j);
                if (c == 'S') { x = i; y = j; }
                else if (c == 'L') d[i][j] = cnt++;
            }
        }
        if (cnt == 0) return 0;
        boolean[][][][] vis = new boolean[m][n][energy + 1][1 << cnt];
        List<int[]> q = new ArrayList<>();
        q.add(new int[] {x, y, energy, (1 << cnt) - 1});
        vis[x][y][energy][(1 << cnt) - 1] = true;
        int[] dirs = {-1, 0, 1, 0, -1};
        int ans = 0;
        while (!q.isEmpty()) {
            List<int[]> t = q;
            q = new ArrayList<>();
            for (int[] s : t) {
                int i = s[0], j = s[1], curEnergy = s[2], mask = s[3];
                if (mask == 0) return ans;
                if (curEnergy <= 0) continue;
                for (int k = 0; k < 4; k++) {
                    int nx = i + dirs[k], ny = j + dirs[k + 1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && classroom[nx].charAt(ny) != 'X') {
                        int nxtEnergy = classroom[nx].charAt(ny) == 'R' ? energy : curEnergy - 1;
                        int nxtMask = mask;
                        if (classroom[nx].charAt(ny) == 'L') nxtMask &= ~(1 << d[nx][ny]);
                        if (!vis[nx][ny][nxtEnergy][nxtMask]) {
                            vis[nx][ny][nxtEnergy][nxtMask] = true;
                            q.add(new int[] {nx, ny, nxtEnergy, nxtMask});
                        }
                    }
                }
            }
            ans++;
        }
        return -1;
    }
}
