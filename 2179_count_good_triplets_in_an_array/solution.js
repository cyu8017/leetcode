// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var goodTriplets = function(nums1, nums2) {
    const n = nums1.length;
    const pos2 = new Array(n);
    for (let i = 0; i < n; i++) pos2[nums2[i]] = i;
    const mapped = new Array(n);
    for (let i = 0; i < n; i++) mapped[i] = pos2[nums1[i]];
    const left = new Array(n).fill(0), right = new Array(n).fill(0);
    const makeFenwick = (sz) => {
        const bit = new Array(sz).fill(0);
        return {
            add(i, v) { for (; i < bit.length; i += i & -i) bit[i] += v; },
            sum(i) { let s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; },
        };
    };
    let fw = makeFenwick(n + 2);
    for (let i = 0; i < n; i++) {
        left[i] = fw.sum(mapped[i]);
        fw.add(mapped[i] + 1, 1);
    }
    fw = makeFenwick(n + 2);
    for (let i = n - 1; i >= 0; i--) {
        right[i] = fw.sum(n) - fw.sum(mapped[i] + 1);
        fw.add(mapped[i] + 1, 1);
    }
    let ans = 0;
    for (let i = 0; i < n; i++) ans += left[i] * right[i];
    return ans;
};
