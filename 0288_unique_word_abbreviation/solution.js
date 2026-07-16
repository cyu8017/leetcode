// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

class ValidWordAbbr {
    /**
     * @param {string[]} dictionary
     */
    constructor(dictionary) {
        this.groups = new Map();
        for (const word of dictionary) {
            const key = ValidWordAbbr.abbreviate(word);
            if (!this.groups.has(key)) {
                this.groups.set(key, new Set());
            }
            this.groups.get(key).add(word);
        }
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    isUnique(word) {
        const key = ValidWordAbbr.abbreviate(word);
        const words = this.groups.get(key);
        return !words || (words.size === 1 && words.has(word));
    }

    /**
     * @param {string} word
     * @return {string}
     */
    static abbreviate(word) {
        if (word.length <= 2) {
            return word;
        }
        return `${word[0]}${word.length - 2}${word[word.length - 1]}`;
    }
}

module.exports = { ValidWordAbbr };
