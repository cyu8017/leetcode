// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

int minimumOperations(int* nums, int numsSize) {
    int l = 0, r = numsSize - 1;
    long long left = nums[l], right = nums[r];
    int ans = 0;
    while (l < r) {
        if (left == right) {
            l++; r--;
            if (l < r) { left = nums[l]; right = nums[r]; }
        } else if (left < right) {
            l++; left += nums[l]; ans++;
        } else {
            r--; right += nums[r]; ans++;
        }
    }
    return ans;
}
