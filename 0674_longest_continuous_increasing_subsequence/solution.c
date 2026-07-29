// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

int findLengthOfLCIS(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int best = 1, cur = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > nums[i - 1]) {
            cur++;
            if (cur > best) best = cur;
        } else cur = 1;
    }
    return best;
}
