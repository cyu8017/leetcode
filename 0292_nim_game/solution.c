// LeetCode 0292 - Nim Game
// https://leetcode.com/problems/nim-game/

#include <stdbool.h>

bool canWinNim(int n) {
    return n % 4 != 0;
}
