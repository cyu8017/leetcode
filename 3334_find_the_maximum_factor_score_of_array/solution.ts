// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

function gcd(a: any, b: any): any {
    while (b !== 0) { const t = a % b; a = b; b = t; }
    return a;
}function lcm(a: any, b: any): any { return a / gcd(a, b) * b; }export function maxScore(nums: any): any {
    const n = nums.length;
    let gcdAll = nums[0], lcmAll = nums[0];
    for (let i = 1; i < n; i++) {
        gcdAll = gcd(gcdAll, nums[i]);
        lcmAll = lcm(lcmAll, nums[i]);
    }
    let ans = gcdAll * lcmAll;
    for (let skip = 0; skip < n; skip++) {
        let g = 0, l = 1;
        let first = true;
        for (let i = 0; i < n; i++) {
            if (i === skip) continue;
            if (first) { g = l = nums[i]; first = false; }
            else { g = gcd(g, nums[i]); l = lcm(l, nums[i]); }
        }
        if (first) continue;
        const v = g * l;
        if (v > ans) ans = v;
    }
    return ans;
}
