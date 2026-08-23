// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

/**
 * @param {number[][]} items1
 * @param {number[][]} items2
 * @return {number[][]}
 */
var mergeSimilarItems = function(items1, items2) {
    const mp = new Map();
    for (const it of items1) mp.set(it[0], (mp.get(it[0]) || 0) + it[1]);
    for (const it of items2) mp.set(it[0], (mp.get(it[0]) || 0) + it[1]);
    return [...mp.entries()].sort((a, b) => a[0] - b[0]).map(([k, v]) => [k, v]);
};
