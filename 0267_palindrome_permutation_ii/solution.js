// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

/**
 * @param {string} s
 * @return {string[]}
 */
var generatePalindromes = function(s) {
    const counts = new Map();
    for (const char of s) {
        counts.set(char, (counts.get(char) || 0) + 1);
    }

    let middle = '';
    const oddChars = [];
    for (const [char, count] of counts) {
        if (count % 2) {
            oddChars.push(char);
        }
    }
    if (oddChars.length > 1) {
        return [];
    }
    if (oddChars.length === 1) {
        middle = oddChars[0];
    }

    const half = [];
    for (const char of [...counts.keys()].sort()) {
        half.push(...Array(counts.get(char) / 2).fill(char));
    }

    const result = [];
    const used = new Array(half.length).fill(false);
    const path = [];

    const backtrack = () => {
        if (path.length === half.length) {
            const prefix = path.join('');
            result.push(prefix + middle + prefix.split('').reverse().join(''));
            return;
        }
        for (let index = 0; index < half.length; index++) {
            if (used[index]) {
                continue;
            }
            if (index > 0 && half[index] === half[index - 1] && !used[index - 1]) {
                continue;
            }
            used[index] = true;
            path.push(half[index]);
            backtrack();
            path.pop();
            used[index] = false;
        }
    };

    backtrack();
    return result;
};
