// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {string[]}
 */
var wordSubsets = function(words1, words2) {
    const need = new Array(26).fill(0);
    for (const w of words2) {
        const cnt = new Array(26).fill(0);
        for (const c of w) cnt[c.charCodeAt(0) - 97]++;
        for (let i = 0; i < 26; i++) need[i] = Math.max(need[i], cnt[i]);
    }
    const ans = [];
    for (const w of words1) {
        const cnt = new Array(26).fill(0);
        for (const c of w) cnt[c.charCodeAt(0) - 97]++;
        let ok = true;
        for (let i = 0; i < 26; i++) if (cnt[i] < need[i]) { ok = false; break; }
        if (ok) ans.push(w);
    }
    return ans;
};
