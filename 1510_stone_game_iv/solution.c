// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

#include <stdlib.h>
#include <stdbool.h>

bool winnerSquareGame(int n) {
    bool* win = (bool*)calloc((size_t)n + 1, sizeof(bool));
    for (int value = 1; value <= n; value++) {
        for (int root = 1; root * root <= value; root++) {
            if (!win[value - root * root]) {
                win[value] = true;
                break;
            }
        }
    }
    bool ans = win[n];
    free(win);
    return ans;
}
