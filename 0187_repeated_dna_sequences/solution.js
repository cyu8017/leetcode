// LeetCode 0187 - Repeated DNA Sequences
// https://leetcode.com/problems/repeated-dna-sequences/

/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    const seen = new Set();
    const repeated = new Set();

    for (let i = 0; i <= s.length - 10; i++) {
        const sequence = s.slice(i, i + 10);
        if (seen.has(sequence)) {
            repeated.add(sequence);
        } else {
            seen.add(sequence);
        }
    }

    return [...repeated];
};