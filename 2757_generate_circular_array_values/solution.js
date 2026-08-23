// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

/**
 * @param {Array} arr
 * @param {number} startIndex
 * @yields {number}
 */
var cycleGenerator = function*(arr, startIndex) {
    let i = startIndex;
    let jump = yield arr[i];
    while (true) {
        const n = arr.length;
        i = ((i + (jump || 0)) % n + n) % n;
        jump = yield arr[i];
    }
};
