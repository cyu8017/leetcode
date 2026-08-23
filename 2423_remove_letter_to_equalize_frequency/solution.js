// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

/**
 * @param {string} word
 * @return {boolean}
 */
var equalFrequency = function(word) {
    for (let skip = 0; skip < word.length; skip++) {
        const cnt = Array(26).fill(0);
        for (let i = 0; i < word.length; i++) {
            if (i === skip) continue;
            cnt[word.charCodeAt(i) - 97]++;
        }
        const freq = new Map();
        for (const c of cnt) {
            if (c > 0) freq.set(c, (freq.get(c) || 0) + 1);
        }
        if (freq.size === 1) return true;
    }
    return false;
};
