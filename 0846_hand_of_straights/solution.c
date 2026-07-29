// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

#include <stdbool.h>
#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

bool isNStraightHand(int* hand, int handSize, int groupSize) {
    if (handSize % groupSize) return false;
    qsort(hand, (size_t)handSize, sizeof(int), cmp_int);
    // count unique
    int* vals = (int*)malloc((size_t)handSize * sizeof(int));
    int* cnt = (int*)malloc((size_t)handSize * sizeof(int));
    int nu = 0;
    for (int i = 0; i < handSize; ) {
        int j = i;
        while (j < handSize && hand[j] == hand[i]) j++;
        vals[nu] = hand[i];
        cnt[nu] = j - i;
        nu++;
        i = j;
    }
    for (int i = 0; i < nu; i++) {
        while (cnt[i] > 0) {
            for (int k = 0; k < groupSize; k++) {
                int need = vals[i] + k;
                int found = -1;
                for (int t = i; t < nu; t++) if (vals[t] == need) { found = t; break; }
                if (found < 0 || cnt[found] == 0) {
                    free(vals); free(cnt);
                    return false;
                }
                cnt[found]--;
            }
        }
    }
    free(vals); free(cnt);
    return true;
}
