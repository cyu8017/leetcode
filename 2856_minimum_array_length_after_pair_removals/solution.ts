// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

export function minLengthAfterRemovals(nums: number[]): number {
    const n = nums.length;
    const freq = new Map();
    let mx = 0;
    for (const v of nums) {
        const c = (freq.get(v) || 0) + 1;
        freq.set(v, c);
        if (c > mx) mx = c;
    }
    if (mx <= Math.floor(n / 2)) return n % 2;
    return 2 * mx - n;
}
