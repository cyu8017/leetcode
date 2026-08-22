// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

#include <stdlib.h>
#include <string.h>

int minimumCardPickup(int* cards, int cardsSize) {
    int maxv = 1000001;
    int* last = (int*)malloc((size_t)maxv * sizeof(int));
    memset(last, -1, (size_t)maxv * sizeof(int));
    int ans = -1;
    for (int i = 0; i < cardsSize; i++) {
        int c = cards[i];
        if (last[c] != -1) {
            int diff = i - last[c] + 1;
            if (ans == -1 || diff < ans) ans = diff;
        }
        last[c] = i;
    }
    free(last);
    return ans;
}
