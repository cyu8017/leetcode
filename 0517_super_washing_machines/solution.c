// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

#include <stdlib.h>

static int absInt(int value) {
    return value < 0 ? -value : value;
}

int findMinMoves(int* machines, int machinesSize) {
    long long total = 0;
    for (int index = 0; index < machinesSize; index++) {
        total += machines[index];
    }
    if (total % machinesSize != 0) {
        return -1;
    }
    const int target = (int)(total / machinesSize);
    long long prefix = 0;
    int result = 0;
    for (int index = 0; index < machinesSize; index++) {
        const int diff = machines[index] - target;
        prefix += diff;
        const int prefixAbs = (int)(prefix < 0 ? -prefix : prefix);
        if (prefixAbs > result) {
            result = prefixAbs;
        }
        if (absInt(diff) > result) {
            result = absInt(diff);
        }
    }
    return result;
}
