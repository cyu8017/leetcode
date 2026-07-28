// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function(trips, capacity) {
    const diff = new Array(1001).fill(0);
    for (const [num, start, end] of trips) {
        diff[start] += num;
        diff[end] -= num;
    }
    let cur = 0;
    for (const x of diff) {
        cur += x;
        if (cur > capacity) return false;
    }
    return true;
};
