// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

long long maximumValueSum(int* nums, int numsSize, int k, int** edges, int edgesSize, int* edgesColSize) {
    (void)edges; (void)edgesSize; (void)edgesColSize;
    long long f0 = 0, f1 = -0x3f3f3f3fLL;
    for (int i = 0; i < numsSize; i++) {
        long long x = nums[i];
        long long n0 = f0 + x > f1 + (x ^ k) ? f0 + x : f1 + (x ^ k);
        long long n1 = f1 + x > f0 + (x ^ k) ? f1 + x : f0 + (x ^ k);
        f0 = n0; f1 = n1;
    }
    return f0;
}
