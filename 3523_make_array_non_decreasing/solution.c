// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

int maximumPossibleSize(int* nums, int numsSize) {
    int ans = 0, mx = 0;
    for (int i = 0; i < numsSize; i++) {
        if (mx <= nums[i]) {
            ans++;
            mx = nums[i];
        }
    }
    return ans;
}
