// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

class Solution {
    wordsAbbreviation(words) {
        const abbreviate = (word, prefix) => {
            if (prefix + 2 >= word.length) return word;
            const middle = word.length - prefix - 1;
            const candidate = `${word.slice(0, prefix)}${middle}${word.slice(-1)}`;
            return candidate.length < word.length ? candidate : word;
        };
        const prefixes = Array(words.length).fill(1);
        let changed = true;
        while (changed) {
            changed = false;
            const groups = new Map();
            for (let index = 0; index < words.length; index += 1) {
                const key = abbreviate(words[index], prefixes[index]);
                if (!groups.has(key)) groups.set(key, []);
                groups.get(key).push(index);
            }
            for (const indices of groups.values()) {
                if (indices.length > 1) {
                    changed = true;
                    for (const index of indices) prefixes[index] += 1;
                }
            }
        }
        return words.map((word, index) => abbreviate(word, prefixes[index]));
    }
}

module.exports = { Solution };
