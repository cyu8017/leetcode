// LeetCode 1566 - Detect Pattern of Length M Repeated K or More Times
// https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

/**
 * @param {number[]} arr
 * @param {number} m
 * @param {number} k
 * @return {boolean}
 */
var containsPattern = function(arr, m, k) {
    let run = 0;
    for (let i = m; i < arr.length; i++) {
        run = arr[i] === arr[i - m] ? run + 1 : 0;
        if (run >= m * (k - 1)) return true;
    }
    return false;
};
