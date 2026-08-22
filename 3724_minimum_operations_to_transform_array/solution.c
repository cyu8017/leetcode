// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

static int imax(int a, int b) { return a > b ? a : b; }
static int imin(int a, int b) { return a < b ? a : b; }
static int iabs(int x) { return x < 0 ? -x : x; }

long long minOperations(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    long long ans = 1;
    int n = nums1Size;
    int ok = 0;
    int d = 1 << 30;
    for (int i = 0; i < n; i++) {
        int x = imax(nums1[i], nums2[i]);
        int y = imin(nums1[i], nums2[i]);
        ans += x - y;
        int t1 = iabs(x - nums2[n]);
        int t2 = iabs(y - nums2[n]);
        int m = imin(t1, t2);
        if (m < d) d = m;
        if (nums2[n] >= y && nums2[n] <= x) ok = 1;
    }
    if (!ok) ans += d;
    return ans;
}
