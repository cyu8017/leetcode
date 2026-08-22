// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int numberOfCleanRooms(int** room, int roomSize, int* roomColSize) {
    int m = roomSize, n = roomColSize[0];
    int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    bool vis[m][n][4];
    memset(vis, 0, sizeof(vis));
    bool cleaned[m][n];
    memset(cleaned, 0, sizeof(cleaned));
    cleaned[0][0] = true;
    int r = 0, c = 0, d = 0, ans = 1;
    while (!vis[r][c][d]) {
        vis[r][c][d] = true;
        int nr = r + dirs[d][0], nc = c + dirs[d][1];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr][nc] == 0) {
            r = nr; c = nc;
            if (!cleaned[r][c]) { cleaned[r][c] = true; ans++; }
        } else d = (d + 1) % 4;
    }
    return ans;
}
