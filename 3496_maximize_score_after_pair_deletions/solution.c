// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

int maximizeScore(int* nums, int numsSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    if (numsSize % 2 == 1) {
        int mn = nums[0];
        for (int i = 0; i < numsSize; i++) if (nums[i] < mn) mn = nums[i];
        return total - mn;
    }
    int mn = nums[0] + nums[1];
    for (int i = 0; i + 1 < numsSize; i++) {
        if (nums[i] + nums[i + 1] < mn) mn = nums[i] + nums[i + 1];
    }
    return total - mn;
}
