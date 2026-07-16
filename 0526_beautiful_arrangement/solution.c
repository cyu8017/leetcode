// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

#include <stdbool.h>

static void backtrack(int index, int n, bool* used, int* count) {
    if (index == n + 1) {
        (*count)++;
        return;
    }
    for (int num = 1; num <= n; num++) {
        if (used[num]) {
            continue;
        }
        if (index % num == 0 || num % index == 0) {
            used[num] = true;
            backtrack(index + 1, n, used, count);
            used[num] = false;
        }
    }
}

int countArrangement(int n) {
    bool used[16] = {false};
    int count = 0;
    backtrack(1, n, used, &count);
    return count;
}
