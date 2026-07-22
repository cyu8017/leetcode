// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

#include <stdlib.h>

typedef struct {
    int* data;
    int size;
} MaxHeap;

static void heapPush(MaxHeap* h, int x) {
    int i = h->size++;
    h->data[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p] >= h->data[i]) break;
        int t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t;
        i = p;
    }
}

static int heapPop(MaxHeap* h) {
    int top = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < h->size && h->data[l] > h->data[best]) best = l;
        if (r < h->size && h->data[r] > h->data[best]) best = r;
        if (best == i) break;
        int t = h->data[i]; h->data[i] = h->data[best]; h->data[best] = t;
        i = best;
    }
    return top;
}

int minimumDeviation(int* nums, int numsSize) {
    MaxHeap h;
    h.data = (int*)malloc((size_t)numsSize * 2 * sizeof(int));
    h.size = 0;
    int mn = 2000000000;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x % 2) x *= 2;
        if (x < mn) mn = x;
        heapPush(&h, x);
    }
    int ans = 2000000000;
    while (1) {
        int x = heapPop(&h);
        if (x - mn < ans) ans = x - mn;
        if (x % 2) break;
        x /= 2;
        if (x < mn) mn = x;
        heapPush(&h, x);
    }
    free(h.data);
    return ans;
}
