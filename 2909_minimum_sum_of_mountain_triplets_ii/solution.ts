// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

export function minimumSum(nums: number[]): number {
    const n = nums.length;
    const left = Array(n), right = Array(n);
    let mn = 1 << 30;
    for (let i = 0; i < n; i++) {
        left[i] = mn;
        if (nums[i] < mn) mn = nums[i];
    }
    mn = 1 << 30;
    for (let i = n - 1; i >= 0; i--) {
        right[i] = mn;
        if (nums[i] < mn) mn = nums[i];
    }
    let ans = 1 << 30;
    for (let j = 1; j < n - 1; j++) {
        if (left[j] < nums[j] && right[j] < nums[j]) {
            const cand = left[j] + nums[j] + right[j];
            if (cand < ans) ans = cand;
        }
    }
    return ans === (1 << 30) ? -1 : ans;
}
