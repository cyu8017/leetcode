// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

export function minimumOperations(nums: number[]): number {
    let l = 0, r = nums.length - 1;
    let left = nums[l], right = nums[r];
    let ans = 0;
    while (l < r) {
        if (left === right) {
            l++;
            r--;
            if (l < r) {
                left = nums[l];
                right = nums[r];
            }
        } else if (left < right) {
            l++;
            left += nums[l];
            ans++;
        } else {
            r--;
            right += nums[r];
            ans++;
        }
    }
    return ans;
}
