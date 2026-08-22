// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

#include <string.h>
#include <stdbool.h>

int shortestSequence(int* rolls, int rollsSize, int k) {
    bool seen[100001];
    memset(seen, 0, sizeof(seen));
    int count = 0, ans = 1;
    for (int i = 0; i < rollsSize; i++) {
        int r = rolls[i];
        if (!seen[r]) { seen[r] = true; count++; }
        if (count == k) {
            ans++;
            memset(seen, 0, (size_t)(k + 1) * sizeof(bool));
            count = 0;
        }
    }
    return ans;
}
