// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var numMatchingSubseq = function(s, words) {
    const waiting = Array.from({ length: 26 }, () => []);
    for (let i = 0; i < words.length; i++) {
        const w = words[i];
        waiting[w.charCodeAt(0) - 97].push([i, 0]);
    }
    let ans = 0;
    for (const ch of s) {
        const cur = waiting[ch.charCodeAt(0) - 97];
        waiting[ch.charCodeAt(0) - 97] = [];
        for (const [wi, idx0] of cur) {
            const idx = idx0 + 1;
            if (idx === words[wi].length) ans++;
            else waiting[words[wi].charCodeAt(idx) - 97].push([wi, idx]);
        }
    }
    return ans;
};
