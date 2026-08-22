// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

#include <stdlib.h>

static int cmp_desc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (y > x) - (y < x);
}

static void heap_up(int* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] <= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}

static void heap_down(int* h, int n, int i) {
    while (1) {
        int l = i * 2 + 1, r = l + 1, s = i;
        if (l < n && h[l] < h[s]) s = l;
        if (r < n && h[r] < h[s]) s = r;
        if (s == i) break;
        int t = h[i]; h[i] = h[s]; h[s] = t;
        i = s;
    }
}

long long maxSum(int** grid, int gridSize, int* gridColSize, int* limits, int limitsSize, int k) {
    (void)limitsSize;
    int* heap = (int*)malloc((size_t)(k + 1) * sizeof(int));
    int hsz = 0;
    long long sum = 0;
    for (int i = 0; i < gridSize; i++) {
        int cols = gridColSize[i];
        int* r = (int*)malloc((size_t)cols * sizeof(int));
        for (int j = 0; j < cols; j++) r[j] = grid[i][j];
        qsort(r, (size_t)cols, sizeof(int), cmp_desc);
        int lim = limits[i];
        if (lim > cols) lim = cols;
        for (int j = 0; j < lim; j++) {
            heap[hsz] = r[j];
            heap_up(heap, hsz);
            hsz++;
            sum += r[j];
            if (hsz > k) {
                sum -= heap[0];
                heap[0] = heap[--hsz];
                if (hsz > 0) heap_down(heap, hsz, 0);
            }
        }
        free(r);
    }
    free(heap);
    return sum;
}
