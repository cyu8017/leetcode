// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    let greatest = -1;
    for (let i = arr.length - 1; i >= 0; i--) {
        const current = arr[i];
        arr[i] = greatest;
        greatest = Math.max(greatest, current);
    }
    return arr;
};
