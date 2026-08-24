// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

export function unequalTriplets(nums: number[]): number {
    const cnt = new Map();
    for (const x of nums) cnt.set(x, (cnt.get(x) || 0) + 1);
    let ans = 0, left = 0;
    const n = nums.length;
    for (const c of cnt.values()) {
        const right = n - left - c;
        ans += left * c * right;
        left += c;
    }
    return ans;
}
