// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

#include <stdbool.h>

bool doesValidArrayExist(int* derived, int derivedSize) {
    int x = 0;
    for (int i = 0; i < derivedSize; i++) x ^= derived[i];
    return x == 0;
}
