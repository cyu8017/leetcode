// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

export function minMaxSubarraySum(nums: any, k: any): any {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let mn = nums[i], mx = nums[i];
        for (let j = i; j < n && j - i + 1 <= k; j++) {
            if (nums[j] < mn) mn = nums[j];
            if (nums[j] > mx) mx = nums[j];
            ans += mn + mx;
        }
    }
    return ans;
}
