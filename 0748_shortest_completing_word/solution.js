// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

/**
 * @param {string} licensePlate
 * @param {string[]} words
 * @return {string}
 */
var shortestCompletingWord = function(licensePlate, words) {
    const need = new Array(26).fill(0);
    for (const ch of licensePlate) {
        const lower = ch.toLowerCase();
        if (lower >= 'a' && lower <= 'z') need[lower.charCodeAt(0) - 97]++;
    }
    let best = '';
    for (const word of words) {
        const counts = new Array(26).fill(0);
        for (const ch of word) counts[ch.charCodeAt(0) - 97]++;
        let ok = true;
        for (let i = 0; i < 26; i++) if (counts[i] < need[i]) { ok = false; break; }
        if (ok && (best.length === 0 || word.length < best.length)) best = word;
    }
    return best;
};
