// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

#include <stdlib.h>

static int cmpItems(const void* a, const void* b) {
    int* ia = *(int**)a;
    int* ib = *(int**)b;
    double ra = (double)ia[0] / (double)ia[1];
    double rb = (double)ib[0] / (double)ib[1];
    if (ra > rb) return -1;
    if (ra < rb) return 1;
    return 0;
}

double maxPrice(int** items, int itemsSize, int* itemsColSize, int capacity) {
    (void)itemsColSize;
    qsort(items, (size_t)itemsSize, sizeof(int*), cmpItems);
    double ans = 0.0;
    int remain = capacity;
    for (int i = 0; i < itemsSize; i++) {
        int price = items[i][0], weight = items[i][1];
        if (remain >= weight) {
            ans += (double)price;
            remain -= weight;
        } else {
            ans += (double)price * (double)remain / (double)weight;
            remain = 0;
            break;
        }
    }
    if (remain > 0) return -1.0;
    return ans;
}
