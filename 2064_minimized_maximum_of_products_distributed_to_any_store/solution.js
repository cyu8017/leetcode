// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

/**
 * @param {number} n
 * @param {number[]} quantities
 * @return {number}
 */
var minimizedMaximum = function(n, quantities) {
    const can = (x) => {
        let need = 0;
        for (const q of quantities) {
            need += Math.floor((q + x - 1) / x);
            if (need > n) return false;
        }
        return true;
    };
    let lo = 1, hi = 0;
    for (const q of quantities) hi = Math.max(hi, q);
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (can(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
