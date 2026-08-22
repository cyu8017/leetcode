// LeetCode 3946 - Maximum Number Of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

#include <stdlib.h>
#include <limits.h>

int maximumSaleItems(int** items, int itemsSize, int* itemsColSize, int budget) {
    (void)itemsColSize;
    int* f = calloc((size_t)(budget + 1), sizeof(int));
    int mn = INT_MAX;
    for (int i = 0; i < itemsSize; i++) {
        int factor = items[i][0], price = items[i][1];
        if (price < mn) mn = price;
        int cnt = 0;
        for (int j = 0; j < itemsSize; j++) if (items[j][0] % factor == 0) cnt++;
        for (int j = budget; j >= price; j--) {
            if (f[j - price] + cnt > f[j]) f[j] = f[j - price] + cnt;
        }
    }
    int ans = 0;
    for (int i = 0; i <= budget; i++) {
        int extra = (budget - i) / mn;
        if (f[i] + extra > ans) ans = f[i] + extra;
    }
    free(f);
    return ans;
}
