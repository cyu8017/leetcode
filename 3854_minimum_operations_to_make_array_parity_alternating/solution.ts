// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

function f(nums: any, k: any, mn: any, mx: any): any {
    let cnt = 0, a = Infinity, b = -Infinity;
    for (let i = 0; i < nums.length; i++) {
        let x = nums[i];
        if (((x - i) & 1) !== k) {
            cnt++;
            if (x === mn) x++;
            else if (x === mx) x--;
        }
        a = Math.min(a, x);
        b = Math.max(b, x);
    }
    return [cnt, Math.max(1, b - a)];
}export function makeParityAlternating(nums: any): any {
    if (nums.length === 1) return [0, 0];
    let mn = nums[0], mx = nums[0];
    for (const x of nums) { mn = Math.min(mn, x); mx = Math.max(mx, x); }
    const r0 = f(nums, 0, mn, mx);
    const r1 = f(nums, 1, mn, mx);
    if (r0[0] !== r1[0]) return r0[0] < r1[0] ? r0 : r1;
    return r0[1] <= r1[1] ? r0 : r1;
}
