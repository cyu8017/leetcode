// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[][]} queries
 * @return {number[]}
 */
var maximumSumQueries = function(nums1, nums2, queries) {
    const n = nums1.length;
    const pts = Array.from({length: n}, (_, i) => [nums1[i], nums2[i], nums1[i] + nums2[i]]);
    pts.sort((a, b) => b[0] - a[0]);
    const qs = queries.map((q, i) => [q[0], q[1], i]);
    qs.sort((a, b) => b[0] - a[0]);
    const ys = [...nums2, ...queries.map(q => q[1])].sort((a, b) => a - b);
    const uniq = [];
    for (const y of ys) if (!uniq.length || uniq[uniq.length - 1] !== y) uniq.push(y);
    const m = uniq.length;
    const bit = Array(m + 2).fill(-1);
    const rank = (y) => {
        let lo = 0, hi = m;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (uniq[mid] < y) lo = mid + 1;
            else hi = mid;
        }
        return lo + 1;
    };
    const update = (i, v) => {
        for (; i <= m; i += i & -i) bit[i] = Math.max(bit[i], v);
    };
    const query = (i) => {
        let best = -1;
        for (; i > 0; i -= i & -i) best = Math.max(best, bit[i]);
        return best;
    };
    const ans = Array(queries.length);
    let j = 0;
    for (const q of qs) {
        while (j < n && pts[j][0] >= q[0]) {
            update(m - rank(pts[j][1]) + 1, pts[j][2]);
            j++;
        }
        ans[q[2]] = query(m - rank(q[1]) + 1);
    }
    return ans;
};
