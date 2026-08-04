// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

/**
 * @param {string} word
 * @return {number}
 */
var wonderfulSubstrings = function(word) {
    const count = new Array(1024).fill(0);
    count[0] = 1;
    let mask = 0, ans = 0;
    for (const ch of word) {
        mask ^= 1 << (ch.charCodeAt(0) - 97);
        ans += count[mask];
        for (let bit = 0; bit < 10; bit++) ans += count[mask ^ (1 << bit)];
        count[mask]++;
    }
    return ans;
};
