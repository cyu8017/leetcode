// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

export class BIT {
    constructor(n: any) {
    this.n = n;
    this.c = new Array(n + 1).fill(0);
}
    update(x: any, delta: any): any {
    for (; x <= this.n; x += x & -x) this.c[x] += delta;
}
    query(x: any): any {
    let sum = 0;
    for (; x > 0; x -= x & -x) sum += this.c[x];
    return sum;
}
}

export function countRatioSubarrays(nums: any, a: any, b: any): any {
    const n = nums.length;
    const s = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        if (nums[i] % 2 === 1) s[i + 1] = s[i] + a;
        else s[i + 1] = s[i] - b;
    }
    let st = s.slice();
    st.sort((x, y) => x - y);
    let uniq = 0;
    for (let i = 0; i < st.length; i++) {
        if (uniq === 0 || st[i] !== st[uniq - 1]) st[uniq++] = st[i];
    }
    st = st.slice(0, uniq);
    const bit = new BIT(st.length + 1);
    let ans = 0;
    for (const v of s) {
        const x = lowerBound(st, v) + 1;
        ans += bit.query(x);
        bit.update(x, 1);
    }
    return ans;
}
function lowerBound(a: any, x: any): any {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >>> 1;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
