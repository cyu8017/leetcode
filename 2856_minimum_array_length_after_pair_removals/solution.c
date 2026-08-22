// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

int minLengthAfterRemovals(int* nums, int numsSize) {
    int n = numsSize, mx = 0, cur = 1;
    for (int i = 1; i < n; i++) {
        if (nums[i] == nums[i - 1]) cur++;
        else { if (cur > mx) mx = cur; cur = 1; }
    }
    if (cur > mx) mx = cur;
    if (mx <= n / 2) return n % 2;
    return 2 * mx - n;
}
