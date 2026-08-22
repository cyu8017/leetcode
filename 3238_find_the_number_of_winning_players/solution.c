// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

#include <string.h>

int winningPlayerCount(int n, int** pick, int pickSize, int* pickColSize) {
    (void)pickColSize;
    int cnt[n][11];
    memset(cnt, 0, sizeof(cnt));
    int win[n];
    memset(win, 0, sizeof(win));
    for (int i = 0; i < pickSize; i++) {
        int x = pick[i][0], y = pick[i][1];
        cnt[x][y]++;
        if (cnt[x][y] > x) win[x] = 1;
    }
    int ans = 0;
    for (int i = 0; i < n; i++) ans += win[i];
    return ans;
}
