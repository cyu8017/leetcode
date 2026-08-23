// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

/**
 * @param {string[]} sentences
 * @param {number[]} times
 */
var AutocompleteSystem = function(sentences, times) {
    this.counts = new Map();
    this.current = "";
    for (let i = 0; i < sentences.length; ++i) {
        this.counts.set(sentences[i], (this.counts.get(sentences[i]) || 0) + times[i]);
    }
};

/**
 * @param {character} c
 * @return {string[]}
 */
AutocompleteSystem.prototype.input = function(c) {
    if (c === "#") {
        const sentence = this.current;
        this.counts.set(sentence, (this.counts.get(sentence) || 0) + 1);
        this.current = "";
        return [];
    }
    this.current += c;
    const prefix = this.current;
    const matches = [];
    for (const sentence of this.counts.keys()) {
        if (sentence.startsWith(prefix)) matches.push(sentence);
    }
    matches.sort((a, b) => {
        const ca = this.counts.get(a), cb = this.counts.get(b);
        if (ca !== cb) return cb - ca;
        return a < b ? -1 : a > b ? 1 : 0;
    });
    return matches.length > 3 ? matches.slice(0, 3) : matches;
};
