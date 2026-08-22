// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

long long minOperations(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    (void)nums2Size;
    if (k == 0) {
        for (int i = 0; i < nums1Size; i++) if (nums1[i] != nums2[i]) return -1;
        return 0;
    }
    long long pos = 0, neg = 0;
    for (int i = 0; i < nums1Size; i++) {
        int d = nums1[i] - nums2[i];
        if (d % k != 0) return -1;
        if (d > 0) pos += d / k;
        else neg += (-d) / k;
    }
    if (pos != neg) return -1;
    return pos;
}
