// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

export function smallestSubarrays(nums: number[]): number[] {
    const n = nums.length;
    const ans = Array(n).fill(0);
    const last = Array(32).fill(-1);
    for (let i = n - 1; i >= 0; i--) {
        for (let b = 0; b < 32; b++)
            if (((nums[i] >> b) & 1) !== 0) last[b] = i;
        let far = i;
        for (let b = 0; b < 32; b++) far = Math.max(far, last[b]);
        ans[i] = far - i + 1;
    }
    return ans;
}
