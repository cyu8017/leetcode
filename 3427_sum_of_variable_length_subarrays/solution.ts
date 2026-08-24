// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

export function subarraySum(nums: any): any {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let start = i - nums[i];
        if (start < 0) start = 0;
        ans += pref[i + 1] - pref[start];
    }
    return ans;
}
