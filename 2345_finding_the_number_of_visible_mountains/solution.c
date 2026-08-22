// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

#include <stdlib.h>

typedef struct { int l, r; } Mt;

static int cmpMt(const void* a, const void* b) {
    const Mt* pa = (const Mt*)a;
    const Mt* pb = (const Mt*)b;
    if (pa->l != pb->l) return pa->l - pb->l;
    return pb->r - pa->r;
}

int visibleMountains(int** peaks, int peaksSize, int* peaksColSize) {
    (void)peaksColSize;
    Mt* arr = (Mt*)malloc((size_t)peaksSize * sizeof(Mt));
    for (int i = 0; i < peaksSize; i++) {
        arr[i].l = peaks[i][0] - peaks[i][1];
        arr[i].r = peaks[i][0] + peaks[i][1];
    }
    qsort(arr, (size_t)peaksSize, sizeof(Mt), cmpMt);
    int ans = 0, maxR = -1 << 30;
    for (int i = 0; i < peaksSize; ) {
        int j = i;
        while (j < peaksSize && arr[j].l == arr[i].l && arr[j].r == arr[i].r) j++;
        if (arr[i].r > maxR) {
            if (j - i == 1) ans++;
            maxR = arr[i].r;
        }
        i = j;
    }
    free(arr);
    return ans;
}
