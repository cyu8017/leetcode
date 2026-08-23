// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    const list = num.slice();
    let i = list.length - 1;
    while (k > 0 || i >= 0) {
        if (i >= 0) {
            k += list[i];
            list[i] = k % 10;
            i--;
        } else {
            list.unshift(k % 10);
        }
        k = Math.floor(k / 10);
    }
    return list;
};
