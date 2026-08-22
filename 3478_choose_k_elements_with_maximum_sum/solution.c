// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

#include <stdlib.h>

typedef struct {
    int v1, v2, i;
} Item3478;

static int cmp_item(const void* a, const void* b) {
    const Item3478* x = (const Item3478*)a;
    const Item3478* y = (const Item3478*)b;
    return (x->v1 > y->v1) - (x->v1 < y->v1);
}

static void hup(int* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] <= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}

static void hdown(int* h, int n, int i) {
    while (1) {
        int l = i * 2 + 1, r = l + 1, s = i;
        if (l < n && h[l] < h[s]) s = l;
        if (r < n && h[r] < h[s]) s = r;
        if (s == i) break;
        int t = h[i]; h[i] = h[s]; h[s] = t;
        i = s;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* findMaxSum(int* nums1, int nums1Size, int* nums2, int nums2Size, int k, int* returnSize) {
    (void)nums2Size;
    int n = nums1Size;
    Item3478* arr = (Item3478*)malloc((size_t)n * sizeof(Item3478));
    for (int i = 0; i < n; i++) {
        arr[i].v1 = nums1[i];
        arr[i].v2 = nums2[i];
        arr[i].i = i;
    }
    qsort(arr, (size_t)n, sizeof(Item3478), cmp_item);
    long long* ans = (long long*)calloc((size_t)n, sizeof(long long));
    int* heap = (int*)malloc((size_t)(k + 1) * sizeof(int));
    int hsz = 0;
    long long sum = 0;
    int i = 0;
    while (i < n) {
        int v = arr[i].v1;
        int start = i;
        while (i < n && arr[i].v1 == v) i++;
        for (int t = start; t < i; t++) ans[arr[t].i] = sum;
        for (int t = start; t < i; t++) {
            heap[hsz] = arr[t].v2;
            hup(heap, hsz);
            hsz++;
            sum += arr[t].v2;
            if (hsz > k) {
                sum -= heap[0];
                heap[0] = heap[--hsz];
                if (hsz > 0) hdown(heap, hsz, 0);
            }
        }
    }
    free(arr);
    free(heap);
    *returnSize = n;
    return ans;
}
