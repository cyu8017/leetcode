// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

#include <stdlib.h>

typedef struct { int key; long long val; } KV;

long long maxScore(int* prices, int pricesSize) {
    KV* best = (KV*)malloc(pricesSize * sizeof(KV));
    int bn = 0;
    long long ans = 0;
    for (int i = 0; i < pricesSize; i++) {
        int key = prices[i] - (i + 1);
        int found = -1;
        for (int j = 0; j < bn; j++) if (best[j].key == key) { found = j; break; }
        long long prev = found >= 0 ? best[found].val : 0;
        long long cand = prev + prices[i];
        if (found >= 0) {
            if (cand > best[found].val) best[found].val = cand;
        } else {
            best[bn].key = key; best[bn].val = cand; bn++;
        }
        long long cur = found >= 0 ? best[found].val : cand;
        if (cur > ans) ans = cur;
    }
    free(best);
    return ans;
}
