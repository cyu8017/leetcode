// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

int dotProduct(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size < nums2Size ? nums1Size : nums2Size;
    long long ans = 0;
    for (int i = 0; i < n; i++) ans += (long long)nums1[i] * nums2[i];
    return (int)ans;
}
