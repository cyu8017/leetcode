// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

int countDigitOccurrences(int* nums, int numsSize, int digit) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        for (; x > 0; x /= 10) if (x % 10 == digit) ans++;
    }
    return ans;
}
