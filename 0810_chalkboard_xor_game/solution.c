// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

#include <stdbool.h>

bool xorGame(int* nums, int numsSize) {
    int x = 0;
    for (int i = 0; i < numsSize; i++) x ^= nums[i];
    return x == 0 || numsSize % 2 == 0;
}
