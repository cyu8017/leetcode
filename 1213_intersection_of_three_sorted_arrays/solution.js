// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number[]} arr3
 * @return {number[]}
 */
var arraysIntersection = function(arr1, arr2, arr3) {
    const s2 = new Set(arr2), s3 = new Set(arr3);
    return [...new Set(arr1)].filter((x) => s2.has(x) && s3.has(x)).sort((a, b) => a - b);
};
