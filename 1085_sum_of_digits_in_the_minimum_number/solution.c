// LeetCode 1085 - Sum of Digits in the Minimum Number
// https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

int sumOfDigits(int* nums, int numsSize) {
    int n = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < n) {
            n = nums[i];
        }
    }
    int digitSum = 0;
    while (n) {
        digitSum += n % 10;
        n /= 10;
    }
    return digitSum % 2 == 0 ? 1 : 0;
}
