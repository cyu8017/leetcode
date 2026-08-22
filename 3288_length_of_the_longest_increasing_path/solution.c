// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

#include <stdlib.h>

typedef struct { int x, y, i; } Pt;

static int cmpPt(const void* a, const void* b) {
    const Pt* p = a, *q = b;
    if (p->x != q->x) return (p->x > q->x) - (p->x < q->x);
    return (q->y > p->y) - (q->y < p->y);
}

static int lis(int* a, int n) {
    int* tails = (int*)malloc((size_t)(n + 1) * sizeof(int));
    int tn = 0;
    for (int i = 0; i < n; i++) {
        int x = a[i];
        int l = 0, r = tn;
        while (l < r) {
            int mid = (l + r) / 2;
            if (tails[mid] < x) l = mid + 1;
            else r = mid;
        }
        if (l == tn) tails[tn++] = x;
        else tails[l] = x;
    }
    free(tails);
    return tn;
}

int maxPathLength(int** coordinates, int coordinatesSize, int* coordinatesColSize, int k) {
    (void)coordinatesColSize;
    int n = coordinatesSize;
    Pt* arr = (Pt*)malloc((size_t)n * sizeof(Pt));
    for (int i = 0; i < n; i++) arr[i] = (Pt){coordinates[i][0], coordinates[i][1], i};
    qsort(arr, (size_t)n, sizeof(Pt), cmpPt);
    int kx = coordinates[k][0], ky = coordinates[k][1];
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* right = (int*)malloc((size_t)n * sizeof(int));
    int ln = 0, rn = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i].x < kx && arr[i].y < ky) left[ln++] = arr[i].y;
        if (arr[i].x > kx && arr[i].y > ky) right[rn++] = arr[i].y;
    }
    int ans = lis(left, ln) + 1 + lis(right, rn);
    free(arr); free(left); free(right);
    return ans;
}
