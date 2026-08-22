// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

#include <stdlib.h>
#include <string.h>

long long minimumTotalCost(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    int* freq = (int*)calloc((size_t)(n + 1), sizeof(int));
    long long ans = 0;
    int same = 0;
    for (int i = 0; i < n; i++) {
        if (nums1[i] == nums2[i]) {
            same++;
            freq[nums1[i]]++;
            ans += i;
        }
    }
    int maxFreq = 0, maxVal = 0;
    for (int v = 1; v <= n; v++) {
        if (freq[v] > maxFreq) { maxFreq = freq[v]; maxVal = v; }
    }
    int need = maxFreq * 2 - same;
    if (need <= 0) { free(freq); return ans; }
    for (int i = 0; i < n && need > 0; i++) {
        if (nums1[i] != nums2[i] && nums1[i] != maxVal && nums2[i] != maxVal) {
            ans += i;
            need--;
        }
    }
    free(freq);
    return need > 0 ? -1 : ans;
}
