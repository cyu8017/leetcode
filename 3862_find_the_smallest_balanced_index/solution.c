// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

int smallestBalancedIndex(int* nums, int numsSize) {
    long long s = 0, p = 1;
    for (int i = 0; i < numsSize; i++) s += nums[i];
    for (int i = numsSize - 1; i >= 0; i--) {
        s -= nums[i];
        if (s == p) return i;
        p *= nums[i];
        if (p >= s) break;
    }
    return -1;
}
