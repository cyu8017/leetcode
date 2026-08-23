// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var isItPossible = function(word1, word2) {
    const c1 = new Array(26).fill(0), c2 = new Array(26).fill(0);
    for (const c of word1) c1[c.charCodeAt(0) - 97]++;
    for (const c of word2) c2[c.charCodeAt(0) - 97]++;
    let d1 = 0, d2 = 0;
    for (let i = 0; i < 26; i++) {
        if (c1[i] > 0) d1++;
        if (c2[i] > 0) d2++;
    }
    for (let a = 0; a < 26; a++) {
        if (c1[a] === 0) continue;
        for (let b = 0; b < 26; b++) {
            if (c2[b] === 0) continue;
            let nd1 = d1, nd2 = d2;
            if (a === b) {
                if (nd1 === nd2) return true;
                continue;
            }
            if (c1[a] === 1) nd1--;
            if (c1[b] === 0) nd1++;
            if (c2[b] === 1) nd2--;
            if (c2[a] === 0) nd2++;
            if (nd1 === nd2) return true;
        }
    }
    return false;
};
