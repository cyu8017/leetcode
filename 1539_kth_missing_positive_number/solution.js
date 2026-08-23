// LeetCode 1539 - Kth Missing Positive Number
// https://leetcode.com/problems/kth-missing-positive-number/

/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    let left = 0, right = arr.length;
    while (left < right) {
        const middle = (left + right) >> 1;
        if (arr[middle] - middle - 1 < k) left = middle + 1;
        else right = middle;
    }
    return left + k;
};
