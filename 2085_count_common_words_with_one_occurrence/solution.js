// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {number}
 */
var countWords = function(words1, words2) {
    const f1 = new Map(), f2 = new Map();
    for (const w of words1) f1.set(w, (f1.get(w) || 0) + 1);
    for (const w of words2) f2.set(w, (f2.get(w) || 0) + 1);
    let ans = 0;
    for (const [k, v] of f1)
        if (v === 1 && (f2.get(k) || 0) === 1) ans++;
    return ans;
};
