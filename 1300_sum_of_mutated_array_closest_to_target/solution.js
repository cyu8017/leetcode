// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var findBestValue = function(arr, target) {
    let lo = 0, hi = Math.max(...arr);
    const sumAt = (v) => arr.reduce((s, x) => s + Math.min(x, v), 0);
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (sumAt(mid) < target) lo = mid + 1;
        else hi = mid;
    }
    const before = sumAt(lo - 1), after = sumAt(lo);
    return target - before <= after - target ? lo - 1 : lo;
};
