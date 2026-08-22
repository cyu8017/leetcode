// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

static int calc(int* a1, int* a2, int n) {
    int ops = 0;
    int last1 = a1[n - 1], last2 = a2[n - 1];
    for (int i = 0; i < n - 1; i++) {
        int x = a1[i], y = a2[i];
        if (x <= last1 && y <= last2) continue;
        if (y <= last1 && x <= last2) { ops++; continue; }
        return 1 << 30;
    }
    return ops;
}

int minOperations(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    int ans = calc(nums1, nums2, n);
    int t = nums1[n - 1]; nums1[n - 1] = nums2[n - 1]; nums2[n - 1] = t;
    int cand = calc(nums1, nums2, n) + 1;
    if (cand < ans) ans = cand;
    /* restore */
    t = nums1[n - 1]; nums1[n - 1] = nums2[n - 1]; nums2[n - 1] = t;
    return ans >= (1 << 30) ? -1 : ans;
}
