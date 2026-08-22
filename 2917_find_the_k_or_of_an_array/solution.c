// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

int findKOr(int* nums, int numsSize, int k) {
    int ans = 0;
    for (int b = 0; b < 31; b++) {
        int cnt = 0;
        for (int i = 0; i < numsSize; i++) if (nums[i] & (1 << b)) cnt++;
        if (cnt >= k) ans |= 1 << b;
    }
    return ans;
}
