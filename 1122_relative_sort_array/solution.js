// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
    const count = new Map();
    for (const x of arr1) count.set(x, (count.get(x) || 0) + 1);
    const ans = [];
    for (const x of arr2) {
        const c = count.get(x) || 0;
        for (let i = 0; i < c; i++) ans.push(x);
        count.delete(x);
    }
    const rest = [...count.keys()].sort((a, b) => a - b);
    for (const x of rest) {
        const c = count.get(x);
        for (let i = 0; i < c; i++) ans.push(x);
    }
    return ans;
};
