// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

function makePal(x: any): any {
    const ch = String(x).split('');
    for (let i = 0, j = ch.length - 1; i < j; i++, j--) ch[j] = ch[i];
    return parseInt(ch.join(''), 10);
}function costOf(nums: any, p: any): any {
    let c = 0;
    for (const v of nums) c += Math.abs(v - p);
    return c;
}export function minimumCost(nums: any): any {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const median = nums[(n / 2) | 0];
    const candidates = [makePal(median)];
    const s = String(median);
    const half = parseInt(s.substring(0, ((s.length + 1) / 2) | 0), 10);
    for (let d = -2; d <= 2; d++) {
        const h = half + d;
        if (h <= 0) continue;
        const hs = String(h);
        let pal;
        if (s.length % 2 === 0) {
            const rb = hs.split('').reverse().join('');
            pal = hs + rb;
        } else {
            const prefix = hs.substring(0, hs.length - 1);
            const rb = prefix.split('').reverse().join('');
            pal = hs + rb;
        }
        const parsed = parseInt(pal, 10);
        if (!Number.isNaN(parsed)) candidates.push(parsed);
    }
    for (const v of [1, 9, 11, 99, 101]) candidates.push(v);
    let ans = Number.MAX_SAFE_INTEGER / 4;
    for (const p of candidates) {
        if (p <= 0) continue;
        ans = Math.min(ans, costOf(nums, p));
    }
    return ans;
}
