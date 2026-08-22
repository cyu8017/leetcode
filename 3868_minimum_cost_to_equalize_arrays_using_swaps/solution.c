// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

#include <stdlib.h>

typedef struct { int key; int cnt; } Pair3868;

static int findp(Pair3868* a, int n, int key) {
    for (int i = 0; i < n; i++) if (a[i].key == key) return i;
    return -1;
}

int minCost(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    Pair3868* cnt2 = (Pair3868*)malloc((size_t)(nums2Size + 8) * sizeof(Pair3868));
    int c2 = 0;
    for (int i = 0; i < nums2Size; i++) {
        int idx = findp(cnt2, c2, nums2[i]);
        if (idx < 0) { cnt2[c2].key = nums2[i]; cnt2[c2].cnt = 1; c2++; }
        else cnt2[idx].cnt++;
    }
    Pair3868* cnt1 = (Pair3868*)malloc((size_t)(nums1Size + 8) * sizeof(Pair3868));
    int c1 = 0;
    for (int i = 0; i < nums1Size; i++) {
        int x = nums1[i];
        int idx2 = findp(cnt2, c2, x);
        if (idx2 >= 0 && cnt2[idx2].cnt > 0) cnt2[idx2].cnt--;
        else {
            int idx = findp(cnt1, c1, x);
            if (idx < 0) { cnt1[c1].key = x; cnt1[c1].cnt = 1; c1++; }
            else cnt1[idx].cnt++;
        }
    }
    int ans = 0;
    for (int i = 0; i < c1; i++) {
        if (cnt1[i].cnt % 2 == 1) { free(cnt1); free(cnt2); return -1; }
        ans += cnt1[i].cnt / 2;
    }
    for (int i = 0; i < c2; i++) {
        if (cnt2[i].cnt % 2 == 1) { free(cnt1); free(cnt2); return -1; }
    }
    free(cnt1); free(cnt2);
    return ans;
}
