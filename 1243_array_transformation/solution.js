// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var transformArray = function(arr) {
    while (true) {
        const nxt = arr.slice();
        for (let i = 1; i < arr.length - 1; i++) {
            if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) nxt[i]++;
            else if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) nxt[i]--;
        }
        if (nxt.every((v, i) => v === arr[i])) return arr;
        arr = nxt;
    }
};
