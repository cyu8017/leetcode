// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function(arr) {
    const n = arr.length;
    const threshold = Math.floor(n / 4);
    for (const idx of [Math.floor(n / 4), Math.floor(n / 2), Math.floor(3 * n / 4)]) {
        const value = arr[idx];
        if (arr.filter((x) => x === value).length > threshold) return value;
    }
    return arr[0];
};
