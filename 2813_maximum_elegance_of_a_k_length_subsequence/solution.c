// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int profit, cat; } Item;
static int cmp_item(const void* a, const void* b) {
    return ((const Item*)b)->profit - ((const Item*)a)->profit;
}

long long findMaximumElegance(int** items, int itemsSize, int* itemsColSize, int k) {
    (void)itemsColSize;
    Item* arr = (Item*)malloc(itemsSize * sizeof(Item));
    for (int i = 0; i < itemsSize; i++) {
        arr[i].profit = items[i][0];
        arr[i].cat = items[i][1];
    }
    qsort(arr, itemsSize, sizeof(Item), cmp_item);
    bool* seen = (bool*)calloc(itemsSize + 5, sizeof(bool)); // cats up to n typically; use hash via array of size itemsSize+1 if cats are 1..n
    // cats can be up to 1e5; use open address
    typedef struct { int key; int used; } SE;
    int htsz = 1; while (htsz < itemsSize * 2 + 16) htsz <<= 1;
    SE* ht = (SE*)calloc(htsz, sizeof(SE));
    int seenCnt = 0;
    long long total = 0;
    int* dup = (int*)malloc(k * sizeof(int));
    int dsz = 0;
    for (int i = 0; i < k; i++) {
        total += arr[i].profit;
        int c = arr[i].cat;
        unsigned h = (unsigned)c & (htsz - 1);
        while (ht[h].used && ht[h].key != c) h = (h + 1) & (htsz - 1);
        if (ht[h].used) dup[dsz++] = arr[i].profit;
        else { ht[h].used = 1; ht[h].key = c; seenCnt++; }
    }
    long long ans = total + (long long)seenCnt * seenCnt;
    for (int i = k; i < itemsSize; i++) {
        int c = arr[i].cat;
        unsigned h = (unsigned)c & (htsz - 1);
        while (ht[h].used && ht[h].key != c) h = (h + 1) & (htsz - 1);
        if (ht[h].used || dsz == 0) continue;
        total += arr[i].profit - dup[--dsz];
        ht[h].used = 1; ht[h].key = c; seenCnt++;
        long long cand = total + (long long)seenCnt * seenCnt;
        if (cand > ans) ans = cand;
    }
    free(arr); free(seen); free(ht); free(dup);
    return ans;
}
