// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

int missingNumber(int* nums, int numsSize) {
    int expected = numsSize * (numsSize + 1) / 2;
    int total = 0;
    for (int index = 0; index < numsSize; ++index) {
        total += nums[index];
    }
    return expected - total;
}
