// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

static int kadane(int* a, int* b, int n) {
    int best = 0, cur = 0, sum = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i];
        cur += b[i] - a[i];
        if (cur < 0) cur = 0;
        if (cur > best) best = cur;
    }
    return sum + best;
}

int maximumsSplicedArray(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int a = kadane(nums1, nums2, nums1Size);
    int b = kadane(nums2, nums1, nums1Size);
    return a > b ? a : b;
}
