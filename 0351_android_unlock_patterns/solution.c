// LeetCode 0351 - Android Unlock Patterns
// https://leetcode.com/problems/android-unlock-patterns/

#include <stdlib.h>

static int jumpMiddle(int last, int nextCell) {
    static const int jumps[81] = {
        -1, -1, 1, -1, -1, -1, 3, -1, 4,
        -1, -1, -1, 2, -1, 4, -1, -1, -1,
        1, -1, -1, -1, 6, -1, -1, -1, 5,
        -1, 2, -1, -1, -1, 5, -1, 6, -1,
        -1, -1, 4, -1, -1, -1, 7, -1, 8,
        -1, -1, -1, 5, -1, -1, -1, 8, -1,
        3, -1, 7, -1, -1, -1, -1, -1, 7,
        -1, -1, -1, 6, -1, 8, -1, -1, -1,
        4, -1, 5, -1, -1, -1, 7, -1, -1,
    };
    return jumps[last * 9 + nextCell];
}

static int absInt(int value) {
    return value < 0 ? -value : value;
}

static int isValid(int visited, int last, int nextCell) {
    if (visited & (1 << nextCell)) {
        return 0;
    }

    int middle = jumpMiddle(last, nextCell);
    if (middle >= 0) {
        return (visited & (1 << middle)) == 0;
    }

    return absInt(last / 3 - nextCell / 3) <= 1
        && absInt(last % 3 - nextCell % 3) <= 1;
}

static int dfs(int visited, int last, int length, int m, int n) {
    if (length > n) {
        return 0;
    }

    int count = (m <= length && length <= n) ? 1 : 0;
    for (int nextCell = 0; nextCell < 9; nextCell++) {
        if (isValid(visited, last, nextCell)) {
            count += dfs(visited | (1 << nextCell), nextCell, length + 1, m, n);
        }
    }

    return count;
}

int numberOfPatterns(int m, int n) {
    return dfs(1 << 0, 0, 1, m, n) * 4
        + dfs(1 << 1, 1, 1, m, n) * 4
        + dfs(1 << 4, 4, 1, m, n);
}
