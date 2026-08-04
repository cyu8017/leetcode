// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

/**
 * @param {string[]} words
 * @param {string[]} puzzles
 * @return {number[]}
 */
var findNumOfValidWords = function(words, puzzles) {
    const maskOf = (s) => {
        let mask = 0;
        for (const ch of s) mask |= 1 << (ch.charCodeAt(0) - 97);
        return mask;
    };
    const freq = new Map();
    for (const w of words) {
        const m = maskOf(w);
        freq.set(m, (freq.get(m) || 0) + 1);
    }
    return puzzles.map((puzzle) => {
        const first = 1 << (puzzle.charCodeAt(0) - 97);
        const full = maskOf(puzzle);
        let sub = full, total = 0;
        while (true) {
            if (sub & first) total += freq.get(sub) || 0;
            if (sub === 0) break;
            sub = (sub - 1) & full;
        }
        return total;
    });
};
