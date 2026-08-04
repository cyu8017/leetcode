// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

/**
 * @param {string[]} words
 * @param {char[]} letters
 * @param {number[]} score
 * @return {number}
 */
var maxScoreWords = function(words, letters, score) {
    const available = new Map();
    for (const ch of letters) available.set(ch, (available.get(ch) || 0) + 1);
    const counts = words.map((word) => {
        const map = new Map();
        for (const ch of word) map.set(ch, (map.get(ch) || 0) + 1);
        return map;
    });
    const values = words.map((word) => {
        let total = 0;
        for (const ch of word) total += score[ch.charCodeAt(0) - 97];
        return total;
    });
    const fits = (need) => {
        for (const [ch, count] of need) {
            if ((available.get(ch) || 0) < count) return false;
        }
        return true;
    };
    const subtract = (need) => {
        for (const [ch, count] of need) available.set(ch, available.get(ch) - count);
    };
    const addBack = (need) => {
        for (const [ch, count] of need) available.set(ch, (available.get(ch) || 0) + count);
    };
    const dfs = (i) => {
        if (i === words.length) return 0;
        let best = dfs(i + 1);
        if (fits(counts[i])) {
            subtract(counts[i]);
            best = Math.max(best, values[i] + dfs(i + 1));
            addBack(counts[i]);
        }
        return best;
    };
    return dfs(0);
};
