// LeetCode 1413 - Minimum Value to Get Positive Step by Step Sum
// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

int minStartValue(int* nums, int numsSize) {
    int prefix = 0, lowest = 0;
    for (int i = 0; i < numsSize; i++) {
        prefix += nums[i];
        if (prefix < lowest) lowest = prefix;
    }
    return 1 - lowest;
}
