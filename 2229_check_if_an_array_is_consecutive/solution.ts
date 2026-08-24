// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

export function isConsecutive(nums: number[]): boolean {
    let mn = nums[0], mx = nums[0];
    const seen = new Set();
    for (const x of nums) {
        if (seen.has(x)) return false;
        seen.add(x);
        mn = Math.min(mn, x);
        mx = Math.max(mx, x);
    }
    return mx - mn + 1 === nums.length;
}
