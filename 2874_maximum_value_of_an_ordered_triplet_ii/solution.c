// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

long long maximumTripletValue(int* nums, int numsSize) {
    long long ans = 0, maxI = 0, maxDiff = 0;
    for (int i = 0; i < numsSize; i++) {
        long long val = nums[i];
        if (maxDiff * val > ans) ans = maxDiff * val;
        if (maxI - val > maxDiff) maxDiff = maxI - val;
        if (val > maxI) maxI = val;
    }
    return ans;
}
