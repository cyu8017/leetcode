// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

function gcd(a: any, b: any): any {
    while (b !== 0) { const t = a % b; a = b; b = t; }
    return a;
}export function maxGcdSum(nums: any, k: any): any {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    let ans = 0;
    let st = [];
    for (let i = 0; i < n; i++) {
        const nst = [[nums[i], i]];
        for (const p of st) {
            const g = gcd(p[0], nums[i]);
            if (nst[nst.length - 1][0] === g) continue;
            nst.push([g, p[1]]);
        }
        st = nst;
        for (const p of st) {
            const g = p[0], idx = p[1];
            if (i - idx + 1 >= k) {
                const cand = (pref[i + 1] - pref[idx]) * g;
                if (cand > ans) ans = cand;
            }
        }
    }
    return ans;
}
