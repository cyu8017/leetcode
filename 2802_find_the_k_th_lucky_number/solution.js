// LeetCode 2802 - Find The K-th Lucky Number
// https://leetcode.com/problems/find-the-k-th-lucky-number/

/**
 * @param {number} k
 * @return {string}
 */
var kthLuckyNumber = function(k) {
    k++;
    let bits = '';
    while (k > 1) {
        if (k % 2 === 0) bits = '4' + bits;
        else bits = '7' + bits;
        k = Math.floor(k / 2);
    }
    return bits;
};
