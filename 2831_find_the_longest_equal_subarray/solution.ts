// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

export function longestEqualSubarray(nums: number[], k: number): number {
    const pos = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (!pos.has(nums[i])) pos.set(nums[i], []);
        pos.get(nums[i]).push(i);
    }
    let ans = 0;
    for (const p of pos.values()) {
        let left = 0;
        for (let right = 0; right < p.length; right++) {
            while (p[right] - p[left] - (right - left) > k) left++;
            ans = Math.max(ans, right - left + 1);
        }
    }
    return ans;
}
