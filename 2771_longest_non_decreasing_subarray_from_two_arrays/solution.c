// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

static int imax(int a, int b) { return a > b ? a : b; }

int maxNonDecreasingLength(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    int dp1 = 1, dp2 = 1, ans = 1;
    for (int i = 1; i < n; i++) {
        int nd1 = 1, nd2 = 1;
        if (nums1[i] >= nums1[i - 1]) nd1 = imax(nd1, dp1 + 1);
        if (nums1[i] >= nums2[i - 1]) nd1 = imax(nd1, dp2 + 1);
        if (nums2[i] >= nums1[i - 1]) nd2 = imax(nd2, dp1 + 1);
        if (nums2[i] >= nums2[i - 1]) nd2 = imax(nd2, dp2 + 1);
        dp1 = nd1; dp2 = nd2;
        ans = imax(ans, imax(dp1, dp2));
    }
    return ans;
}
