// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

int minSwaps(int* nums, int numsSize) {
    int ones = 0;
    for (int i = 0; i < numsSize; i++) ones += nums[i];
    if (ones == 0) return 0;
    int n = numsSize, window = 0;
    for (int i = 0; i < ones; i++) window += nums[i];
    int best = window;
    for (int i = 0; i < n; i++) {
        window -= nums[i];
        window += nums[(i + ones) % n];
        if (window > best) best = window;
    }
    return ones - best;
}
