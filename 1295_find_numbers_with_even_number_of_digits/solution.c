// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

static int digit_count(int value) {
    if (value == 0) return 1;
    int count = 0;
    if (value < 0) value = -value;
    while (value) {
        count++;
        value /= 10;
    }
    return count;
}

int findNumbers(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        if (digit_count(nums[i]) % 2 == 0) ans++;
    }
    return ans;
}
