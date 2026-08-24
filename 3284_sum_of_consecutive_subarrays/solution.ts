// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

export function rangeSum(nums: any): any {
    const mod = 1000000007;
    const n = nums.length;
    let ans = 0, i = 0;
    while (i < n) {
        let j = i;
        while (j + 1 < n && (nums[j + 1] === nums[j] + 1 || nums[j + 1] === nums[j] - 1)) j++;
        for (let L = i; L <= j; L++) {
            let s = 0;
            for (let R = L; R <= j; R++) {
                s += nums[R];
                ans = (ans + s) % mod;
            }
        }
        i = j + 1;
    }
    return ans;
}
