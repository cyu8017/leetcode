// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

/**
 * @param {string[]} words
 * @return {number}
 */
var maximumNumberOfStringPairs = function(words) {
    const freq = new Map();
    let ans = 0;
    for (const w of words) {
        const rev = w.split('').reverse().join('');
        const c = freq.get(rev) || 0;
        if (c > 0) {
            ans++;
            freq.set(rev, c - 1);
        } else {
            freq.set(w, (freq.get(w) || 0) + 1);
        }
    }
    return ans;
};
