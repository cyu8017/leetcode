// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

#include <stdlib.h>

typedef struct { int m, c; } MC;
static int cmp_mc(const void* a, const void* b) {
    return ((const MC*)a)->m - ((const MC*)b)->m;
}

long long* maximumCoins(int* heroes, int heroesSize, int* monsters, int monstersSize, int* coins, int coinsSize, int* returnSize) {
    (void)coinsSize;
    int n = monstersSize;
    MC* arr = (MC*)malloc(n * sizeof(MC));
    for (int i = 0; i < n; i++) { arr[i].m = monsters[i]; arr[i].c = coins[i]; }
    qsort(arr, n, sizeof(MC), cmp_mc);
    long long* pref = (long long*)malloc((n + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + arr[i].c;
    long long* ans = (long long*)malloc(heroesSize * sizeof(long long));
    for (int i = 0; i < heroesSize; i++) {
        int h = heroes[i], lo = 0, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid].m > h) hi = mid;
            else lo = mid + 1;
        }
        ans[i] = pref[lo];
    }
    free(arr); free(pref);
    *returnSize = heroesSize;
    return ans;
}
