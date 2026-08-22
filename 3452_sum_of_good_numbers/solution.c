// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

int sumOfGoodNumbers(int* nums, int numsSize, int k) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int good = 1;
        if (i - k >= 0 && nums[i] <= nums[i - k]) good = 0;
        if (i + k < numsSize && nums[i] <= nums[i + k]) good = 0;
        if (good) ans += nums[i];
    }
    return ans;
}
