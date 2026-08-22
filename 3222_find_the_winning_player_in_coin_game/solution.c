// LeetCode 3222 - Find the Winning Player in Coin Game
// https://leetcode.com/problems/find-the-winning-player-in-coin-game/

#include <stdlib.h>
#include <string.h>

char* losingPlayer(int x, int y) {
    int k = x / 2 < y / 8 ? x / 2 : y / 8;
    x -= 2 * k;
    y -= 8 * k;
    char* ans = malloc(6);
    if (x > 0 && y >= 4) strcpy(ans, "Alice");
    else strcpy(ans, "Bob");
    return ans;
}
