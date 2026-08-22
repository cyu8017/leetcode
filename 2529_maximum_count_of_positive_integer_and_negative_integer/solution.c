// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

int maximumCount(int* nums, int numsSize) {
    int pos = 0, neg = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > 0) pos++;
        else if (nums[i] < 0) neg++;
    }
    return pos > neg ? pos : neg;
}
