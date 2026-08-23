// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

class BITI {
    constructor(n_) { this.n = n_; this.c = new Array(n_ + 1).fill(0); }
    upd(x, d) { for (; x <= this.n; x += x & -x) this.c[x] += d; }
    qry(x) { let s = 0; for (; x > 0; x -= x & -x) s += this.c[x]; return s; }
}
class BITL {
    constructor(n_) { this.n = n_; this.c = new Array(n_ + 1).fill(0); }
    upd(x, d) { for (; x <= this.n; x += x & -x) this.c[x] += d; }
    qry(x) { let s = 0; for (; x > 0; x -= x & -x) s += this.c[x]; return s; }
}
function kth(cnt, m, k) {
    let idx = 0;
    for (let bit = 1 << 20; bit !== 0; bit >>= 1) {
        const nidx = idx + bit;
        if (nidx <= m && cnt.c[nidx] < k) {
            k -= cnt.c[nidx];
            idx = nidx;
        }
    }
    return idx + 1;
}
function sumSmallest(cnt, sum, uniq, m, kk) {
    if (kk <= 0) return 0;
    const r = kth(cnt, m, kk);
    const before = cnt.qry(r - 1);
    let s = sum.qry(r - 1);
    s += (kk - before) * uniq[r - 1];
    return s;
}
function lowerBound(arr, x) {
    let lo = 0, hi = arr.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (arr[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
var minimumCost = function(nums, k, dist) {
    k--;
    const n = nums.length;
    let uniq = nums.slice().sort((a, b) => a - b);
    let write = 0;
    for (let i = 0; i < uniq.length; i++)
        if (write === 0 || uniq[i] !== uniq[write - 1]) uniq[write++] = uniq[i];
    uniq = uniq.slice(0, write);
    const m = uniq.length;
    const cnt = new BITI(m + 2);
    const sum = new BITL(m + 2);
    for (let i = 1; i <= Math.min(dist + 1, n - 1); i++) {
        let r = lowerBound(uniq, nums[i]) + 1;
        cnt.upd(r, 1);
        sum.upd(r, nums[i]);
    }
    const end = Math.min(dist + 1, n - 1);
    let kk = Math.min(k, end);
    let ans = nums[0] + sumSmallest(cnt, sum, uniq, m, kk);
    for (let i = dist + 2; i < n; i++) {
        const rem = nums[i - dist - 1];
        const r1 = lowerBound(uniq, rem) + 1;
        cnt.upd(r1, -1);
        sum.upd(r1, -rem);
        const add = nums[i];
        const r2 = lowerBound(uniq, add) + 1;
        cnt.upd(r2, 1);
        sum.upd(r2, add);
        kk = Math.min(k, dist + 1);
        ans = Math.min(ans, nums[0] + sumSmallest(cnt, sum, uniq, m, kk));
    }
    return ans;
};
