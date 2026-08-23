// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

/**
 * @param {number} k
 * @return {number}
 */
var preimageSizeFZF = function(k) {
    const zeros = (n) => {
        let z = 0;
        while (n > 0) {
            n = Math.floor(n / 5);
            z += n;
        }
        return z;
    };
    const firstGe = (target) => {
        let lo = 0, hi = 5 * target + 5;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (zeros(mid) >= target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    };
    return firstGe(k + 1) - firstGe(k);
};
