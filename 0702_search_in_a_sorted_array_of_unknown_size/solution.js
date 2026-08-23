// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

/**
 * @param {ArrayReader} reader
 * @param {number} target
 * @return {number}
 */
var search = function(reader, target) {
    // Local harness may pass secret array; wrap if needed
    if (Array.isArray(reader)) {
        const secret = reader;
        reader = {
            get(index) {
                if (index < 0 || index >= secret.length) return 2147483647;
                return secret[index];
            }
        };
    }
    let right = 1;
    while (reader.get(right) < target) right <<= 1;
    let left = right >> 1;
    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);
        const value = reader.get(mid);
        if (value === target) return mid;
        if (value > target) right = mid - 1;
        else left = mid + 1;
    }
    return -1;
};
