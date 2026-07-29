// LeetCode 1962 - Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

#include <stdlib.h>

static void heapifyDown(int* h, int n, int i) {
    while (1) {
        int largest = i, l = 2 * i + 1, r = 2 * i + 2;
        if (l < n && h[l] > h[largest]) largest = l;
        if (r < n && h[r] > h[largest]) largest = r;
        if (largest == i) break;
        int t = h[i]; h[i] = h[largest]; h[largest] = t;
        i = largest;
    }
}

static void heapifyUp(int* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] >= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}

int minStoneSum(int* piles, int pilesSize, int k) {
    int* h = (int*)malloc((size_t)pilesSize * sizeof(int));
    for (int i = 0; i < pilesSize; i++) h[i] = piles[i];
    for (int i = pilesSize / 2 - 1; i >= 0; i--) heapifyDown(h, pilesSize, i);
    for (int i = 0; i < k; i++) {
        int x = h[0] - h[0] / 2;
        h[0] = x;
        heapifyDown(h, pilesSize, 0);
    }
    int sum = 0;
    for (int i = 0; i < pilesSize; i++) sum += h[i];
    free(h);
    return sum;
}
