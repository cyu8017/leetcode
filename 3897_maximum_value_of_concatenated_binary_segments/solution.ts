// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

const MOD3897 = 1000000007;
function group3897(p: any): any {
    if (p[1] === 0) return 0;
    if (p[0] > 0) return 1;
    return 2;
}export function maxValue(nums1: any, nums0: any): any {
    const n = nums1.length;
    const pairs = Array.from({length: n}, (_, i) => [nums1[i], nums0[i]]);
    let b = 0;
    for (let i = 0; i < n; i++) b += nums1[i] + nums0[i];
    pairs.sort((a, c) => {
        const g1 = group3897(a), g2 = group3897(c);
        if (g1 !== g2) return g1 - g2;
        if (g1 === 0) return c[0] - a[0];
        if (g1 === 1) {
            if (a[0] !== c[0]) return c[0] - a[0];
            return a[1] - c[1];
        }
        return a[1] - c[1];
    });
    const p = new Array(b);
    p[0] = 1;
    for (let i = 1; i < b; i++) p[i] = Number(2n * BigInt(p[i - 1]) % BigInt(MOD3897));
    let ans = 0;
    b--;
    for (const pr of pairs) {
        let cnt1 = pr[0], cnt0 = pr[1];
        while (cnt1 > 0) {
            ans = (ans + p[b]) % MOD3897;
            b--;
            cnt1--;
        }
        b -= cnt0;
    }
    return ans;
}
