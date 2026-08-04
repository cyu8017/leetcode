// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

/**
 * @param {string} s
 * @param {string} t
 * @param {number} k
 * @return {boolean}
 */
var canConvertString = function(s, t, k) {
    if (s.length !== t.length) return false;
    const used = Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        let shift = (t.charCodeAt(i) - s.charCodeAt(i) + 26) % 26;
        if (shift) {
            used[shift]++;
            if (shift + 26 * (used[shift] - 1) > k) return false;
        }
    }
    return true;
};
