// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

/**
 * @param {number[]} apple
 * @param {number[]} capacity
 * @return {number}
 */
var minimumBoxes = function(apple, capacity) {
    capacity.sort((a, b) => a - b);
    let s = 0;
    for (const x of apple) s += x;
    for (let i = 1; ; i++) {
        s -= capacity[capacity.length - i];
        if (s <= 0) return i;
    }
};
