// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

/**
 * @param {number} target
 * @return {number}
 */
Array.prototype.upperBound = function(target) {
    let lo = 0, hi = this.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (this[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    if (lo === 0 || this[lo - 1] !== target) return -1;
    return lo - 1;
};
