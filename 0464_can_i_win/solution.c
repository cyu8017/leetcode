// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool canWin(int state, int currentTotal, int maxChoosableInteger, int desiredTotal, int* memo) {
    if (memo[state] != 0) {
        return memo[state] == 1;
    }
    for (int pick = 1; pick <= maxChoosableInteger; pick++) {
        int bit = 1 << (pick - 1);
        if (state & bit) {
            continue;
        }
        if (currentTotal + pick >= desiredTotal || !canWin(state | bit, currentTotal + pick, maxChoosableInteger, desiredTotal, memo)) {
            memo[state] = 1;
            return true;
        }
    }
    memo[state] = -1;
    return false;
}

bool canIWin(int maxChoosableInteger, int desiredTotal) {
    if (desiredTotal <= 0) {
        return true;
    }
    int total = maxChoosableInteger * (maxChoosableInteger + 1) / 2;
    if (total < desiredTotal) {
        return false;
    }
    int states = 1 << maxChoosableInteger;
    int* memo = (int*)calloc((size_t)states, sizeof(int));
    bool result = canWin(0, 0, maxChoosableInteger, desiredTotal, memo);
    free(memo);
    return result;
}
