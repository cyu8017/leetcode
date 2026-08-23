// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter {
    /**
     * @param {string[]} words
     */
    constructor(words) {
        this.lookup = new Map();
        for (let index = 0; index < words.length; index++) {
            const word = words[index];
            const size = word.length;
            for (let i = 0; i <= size; i++) {
                for (let j = 0; j <= size; j++) {
                    this.lookup.set(word.substring(0, i) + '#' + word.substring(j), index);
                }
            }
        }
    }

    /**
     * @param {string} pref
     * @param {string} suff
     * @return {number}
     */
    f(pref, suff) {
        const key = pref + '#' + suff;
        return this.lookup.has(key) ? this.lookup.get(key) : -1;
    }
}
