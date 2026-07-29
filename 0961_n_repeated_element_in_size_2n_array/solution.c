// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

int repeatedNTimes(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize && j < i + 4; j++) {
            if (nums[i] == nums[j]) return nums[i];
        }
    }
    return -1;
}
