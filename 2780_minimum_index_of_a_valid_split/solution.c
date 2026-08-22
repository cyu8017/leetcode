// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

int minimumIndex(int* nums, int numsSize) {
    // Boyer-Moore for dominant
    int cand = nums[0], cnt = 0;
    for (int i = 0; i < numsSize; i++) {
        if (cnt == 0) cand = nums[i];
        cnt += (nums[i] == cand) ? 1 : -1;
    }
    int best = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] == cand) best++;
    int left = 0, n = numsSize;
    for (int i = 0; i < n - 1; i++) {
        if (nums[i] == cand) left++;
        int right = best - left;
        if (left * 2 > i + 1 && right * 2 > n - i - 1) return i;
    }
    return -1;
}
