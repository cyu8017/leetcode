// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

/**
 * @param {number[]} arr
 * @return {number}
 */
var missingNumber = function(arr) {
    const diff = (arr[arr.length - 1] - arr[0]) / arr.length;
    for (let i = 1; i < arr.length; i++) {
        const expected = arr[0] + i * diff;
        if (arr[i] !== expected) return expected;
    }
    return arr[0];
};
