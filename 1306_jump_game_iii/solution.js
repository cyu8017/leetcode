// LeetCode 1306 - Jump Game Iii
// https://leetcode.com/problems/jump-game-iii/

/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    const stack = [start], seen = new Set();
    while (stack.length) {
        const i = stack.pop();
        if (seen.has(i) || i < 0 || i >= arr.length) continue;
        if (arr[i] === 0) return true;
        seen.add(i);
        stack.push(i - arr[i], i + arr[i]);
    }
    return false;
};
