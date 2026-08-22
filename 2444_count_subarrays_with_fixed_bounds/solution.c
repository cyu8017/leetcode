// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

long long countSubarrays(int* nums, int numsSize, int minK, int maxK) {
    long long ans = 0;
    int imin = -1, imax = -1, ibad = -1;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x < minK || x > maxK) ibad = i;
        if (x == minK) imin = i;
        if (x == maxK) imax = i;
        int bound = imin < imax ? imin : imax;
        if (bound > ibad) ans += (long long)(bound - ibad);
    }
    return ans;
}
