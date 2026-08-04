// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

/**
 * @param {string} keyboard
 * @param {string} word
 * @return {number}
 */
var calculateTime = function(keyboard, word) {
    const pos = new Map();
    for (let i = 0; i < keyboard.length; i++) pos.set(keyboard[i], i);
    let ans = 0, prev = 0;
    for (const ch of word) {
        ans += Math.abs(pos.get(ch) - prev);
        prev = pos.get(ch);
    }
    return ans;
};
