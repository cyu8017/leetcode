// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var threeEqualParts = function(arr) {
    const ones = [];
    for (let i = 0; i < arr.length; i++) if (arr[i] !== 0) ones.push(i);
    const n = ones.length;
    if (n % 3 !== 0) return [-1, -1];
    if (n === 0) return [0, arr.length - 1];
    const third = n / 3;
    const length = ones[ones.length - 1] - ones[2 * third] + 1;
    const a = ones[0], b = ones[third], c = ones[2 * third];
    if (a + length > arr.length || b + length > arr.length || c + length > arr.length)
        return [-1, -1];
    for (let i = 0; i < length; i++) {
        if (arr[a + i] !== arr[b + i] || arr[a + i] !== arr[c + i]) return [-1, -1];
    }
    return [a + length - 1, b + length];
};
