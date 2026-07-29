// LeetCode 1439 - Find the Kth Smallest Sum of a Matrix With Sorted Rows
// https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

#include <stdlib.h>

typedef struct { int value, i, j; } Item;
typedef struct { Item* data; int size; int cap; } MinHeap;
static void hpush(MinHeap* h, Item v) {
    if (h->size == h->cap) { h->cap *= 2; h->data = (Item*)realloc(h->data, h->cap * sizeof(Item)); }
    int i = h->size++;
    h->data[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].value <= h->data[i].value) break;
        Item t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t; i = p;
    }
}
static Item hpop(MinHeap* h) {
    Item res = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, s = i;
        if (l < h->size && h->data[l].value < h->data[s].value) s = l;
        if (r < h->size && h->data[r].value < h->data[s].value) s = r;
        if (s == i) break;
        Item t = h->data[i]; h->data[i] = h->data[s]; h->data[s] = t; i = s;
    }
    return res;
}

int kthSmallest(int** mat, int matSize, int* matColSize, int k) {
    int* sums = (int*)malloc(sizeof(int));
    int sn = 1; sums[0] = 0;
    for (int r = 0; r < matSize; r++) {
        int cols = matColSize[r];
        MinHeap h = { (Item*)malloc(16 * sizeof(Item)), 0, 16 };
        hpush(&h, (Item){sums[0] + mat[r][0], 0, 0});
        int* merged = (int*)malloc(k * sizeof(int));
        int mn = 0;
        int* seen = (int*)calloc(sn * cols, sizeof(int)); // may be large - use simpler uniqueness via visited pairs in heap carefully
        free(seen);
        // use set via marking visited[i][j] dynamically
        char* vis = (char*)calloc(sn * cols + 1, 1);
        while (h.size && mn < k) {
            Item cur = hpop(&h);
            merged[mn++] = cur.value;
            if (cur.j + 1 < cols) {
                int key = cur.i * cols + (cur.j + 1);
                if (!vis[key]) {
                    vis[key] = 1;
                    hpush(&h, (Item){sums[cur.i] + mat[r][cur.j + 1], cur.i, cur.j + 1});
                }
            }
            if (cur.j == 0 && cur.i + 1 < sn) {
                int key = (cur.i + 1) * cols;
                if (!vis[key]) {
                    vis[key] = 1;
                    hpush(&h, (Item){sums[cur.i + 1] + mat[r][0], cur.i + 1, 0});
                }
            }
        }
        free(vis); free(h.data); free(sums);
        sums = merged; sn = mn;
    }
    int ans = sums[k - 1];
    free(sums);
    return ans;
}
