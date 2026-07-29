// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

#include <stdbool.h>

bool nimGame(int* piles, int pilesSize) {
    int x = 0;
    for (int i = 0; i < pilesSize; i++) x ^= piles[i];
    return x != 0;
}
