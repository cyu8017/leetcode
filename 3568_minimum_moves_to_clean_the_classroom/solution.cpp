// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

#include <string>
#include <vector>

class Solution {
public:
    int minMoves(std::vector<std::string>& classroom, int energy) {
        int m = (int)classroom.size(), n = (int)classroom[0].size();
        std::vector<std::vector<int>> d(m, std::vector<int>(n));
        int x = 0, y = 0, cnt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = classroom[i][j];
                if (c == 'S') {
                    x = i;
                    y = j;
                } else if (c == 'L') {
                    d[i][j] = cnt++;
                }
            }
        }
        if (cnt == 0) return 0;

        std::vector<std::vector<std::vector<std::vector<bool>>>> vis(
            m, std::vector<std::vector<std::vector<bool>>>(
                   n, std::vector<std::vector<bool>>(energy + 1, std::vector<bool>(1 << cnt, false))));
        struct State {
            int i, j, curEnergy, mask;
        };
        std::vector<State> q{{x, y, energy, (1 << cnt) - 1}};
        vis[x][y][energy][(1 << cnt) - 1] = true;
        int dirs[5] = {-1, 0, 1, 0, -1};
        int ans = 0;
        while (!q.empty()) {
            std::vector<State> t = q;
            q.clear();
            for (auto& s : t) {
                int i = s.i, j = s.j, curEnergy = s.curEnergy, mask = s.mask;
                if (mask == 0) return ans;
                if (curEnergy <= 0) continue;
                for (int k = 0; k < 4; k++) {
                    int nx = i + dirs[k], ny = j + dirs[k + 1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && classroom[nx][ny] != 'X') {
                        int nxtEnergy = classroom[nx][ny] == 'R' ? energy : curEnergy - 1;
                        int nxtMask = mask;
                        if (classroom[nx][ny] == 'L') nxtMask &= ~(1 << d[nx][ny]);
                        if (!vis[nx][ny][nxtEnergy][nxtMask]) {
                            vis[nx][ny][nxtEnergy][nxtMask] = true;
                            q.push_back({nx, ny, nxtEnergy, nxtMask});
                        }
                    }
                }
            }
            ans++;
        }
        return -1;
    }
};
