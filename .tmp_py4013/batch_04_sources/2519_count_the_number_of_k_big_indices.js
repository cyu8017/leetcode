// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var kBigIndices = function(nums, k) {
    const Fenwick = function(n) {
        this.bit = Array(n + 2).fill(0);
    };
    Fenwick.prototype.add = function(i, v) {
        for (; i < this.bit.length; i += i & -i) this.bit[i] += v;
    };
    Fenwick.prototype.sum = function(i) {
        let s = 0;
        for (; i > 0; i -= i & -i) s += this.bit[i];
        return s;
    };
    const n = nums.length;
    const uniq = nums.slice().sort((a, b) => a - b);
    let m = 0;
    for (let i = 0; i < uniq.length; i++) {
        if (i === 0 || uniq[i] !== uniq[i - 1]) uniq[m++] = uniq[i];
    }
    const rank = new Map();
    for (let i = 0; i < m; i++) rank.set(uniq[i], i + 1);
    const left = Array(n), right = Array(n);
    let ft = new Fenwick(m);
    for (let i = 0; i < n; i++) {
        const r = rank.get(nums[i]);
        left[i] = ft.sum(r - 1);
        ft.add(r, 1);
    }
    ft = new Fenwick(m);
    for (let i = n - 1; i >= 0; i--) {
        const r = rank.get(nums[i]);
        right[i] = ft.sum(r - 1);
        ft.add(r, 1);
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (left[i] >= k && right[i] >= k) ans++;
    }
    return ans;
};
