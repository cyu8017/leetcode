// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

function upperBound(a, target) {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (a[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
function countInv(nums, k, threshold) {
    const sorted = [];
    let inv = 0;
    for (const num of nums) {
        const left = upperBound(sorted, num);
        const right = upperBound(sorted, num + threshold);
        inv += right - left;
        sorted.splice(upperBound(sorted, num), 0, num);
    }
    return inv >= k;
}
var minThreshold = function(nums, k) {
    let mx = 0;
    for (const v of nums) if (v > mx) mx = v;
    let l = 0, r = mx + 1;
    while (l < r) {
        const m = (l + r) >> 1;
        if (countInv(nums, k, m)) r = m;
        else l = m + 1;
    }
    return l > mx ? -1 : l;
};
