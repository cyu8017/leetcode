// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

export function longestAlternatingSubarray(nums: number[], threshold: number): number {
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        if (nums[i] % 2 !== 0 || nums[i] > threshold) continue;
        let j = i;
        while (j + 1 < n && nums[j + 1] <= threshold && nums[j + 1] % 2 !== nums[j] % 2) j++;
        ans = Math.max(ans, j - i + 1);
    }
    return ans;
}
