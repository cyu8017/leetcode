// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

int dominantIndices(int* nums, int numsSize) {
    int n = numsSize;
    int ans = 0;
    long long suf = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        if ((long long)nums[i] * (n - i - 1) > suf) ans++;
        suf += nums[i];
    }
    return ans;
}
