// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

/**
 * @param {number} n
 * @return {number}
 */
var minimumBoxes = function(n) {
    let height = 0;
    let used = 0;
    let base = 0;
    while (used + ((height + 1) * (height + 2)) / 2 <= n) {
        height++;
        const layer = (height * (height + 1)) / 2;
        used += layer;
        base += height;
    }
    let extra = 0;
    while (used < n) {
        extra++;
        used += extra;
    }
    return base + extra;
};
