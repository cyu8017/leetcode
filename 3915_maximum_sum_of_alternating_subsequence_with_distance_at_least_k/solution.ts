// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

export class Fenwick3915 {
    constructor(n: any) {
    this.f = new Array(n).fill(0);
}
    update(i: any, val: any): any {
    for (; i < this.f.length; i += i & -i) this.f[i] = Math.max(this.f[i], val);
}
    preMax(i: any): any {
    let res = 0;
    for (; i > 0; i &= i - 1) res = Math.max(res, this.f[i]);
    return res;
}
}

export function maxAlternatingSum(nums: any, k: any): any {
    let sorted = nums.slice().sort((a, b) => a - b);
    let m = 0;
    for (let i = 0; i < sorted.length; i++) {
        if (i === 0 || sorted[i] !== sorted[i - 1]) sorted[m++] = sorted[i];
    }
    sorted = sorted.slice(0, m);
    const n = nums.length;
    const fInc = new Array(n).fill(0);
    const fDec = new Array(n).fill(0);
    const inc = new Fenwick3915(m + 1);
    const dec = new Fenwick3915(m + 1);
    let ans = 0;
    const ranks = new Array(n);
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        if (i >= k) {
            const j = ranks[i - k];
            inc.update(m - j, fInc[i - k]);
            dec.update(j + 1, fDec[i - k]);
        }
        let lo = 0, hi = sorted.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (sorted[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        ranks[i] = lo;
        fInc[i] = dec.preMax(lo) + x;
        fDec[i] = inc.preMax(m - 1 - lo) + x;
        ans = Math.max(ans, Math.max(fInc[i], fDec[i]));
    }
    return ans;
}
