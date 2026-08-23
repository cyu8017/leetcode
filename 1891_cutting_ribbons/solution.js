// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

/**
 * @param {number[]} ribbons
 * @param {number} k
 * @return {number}
 */
var maxLength = function(ribbons, k) {
    const can = (length) => {
        let total = 0;
        for (const ribbon of ribbons) total += Math.floor(ribbon / length);
        return total >= k;
    };
    let lo = 1, hi = Math.max(...ribbons);
    while (lo < hi) {
        const mid = (lo + hi + 1) >> 1;
        if (can(mid)) lo = mid;
        else hi = mid - 1;
    }
    return can(lo) ? lo : 0;
};
