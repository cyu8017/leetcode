// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

/**
 * @param {string[]} words
 * @param {number[][]} queries
 * @return {number[]}
 */
var vowelStrings = function(words, queries) {
    const isV = (c) => c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u';
    const n = words.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i];
        const w = words[i];
        if (w.length > 0 && isV(w[0]) && isV(w[w.length - 1])) pref[i + 1]++;
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        ans[i] = pref[queries[i][1] + 1] - pref[queries[i][0]];
    }
    return ans;
};
