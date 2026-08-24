// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

export function countSubarrays(nums: number[], minK: number, maxK: number): number {
    let ans = 0, imin = -1, imax = -1, ibad = -1;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        if (x < minK || x > maxK) ibad = i;
        if (x === minK) imin = i;
        if (x === maxK) imax = i;
        const bound = imin < imax ? imin : imax;
        if (bound > ibad) ans += bound - ibad;
    }
    return ans;
}
