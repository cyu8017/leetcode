// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

export class WordFilter {
    constructor(words: any) {
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

    f(pref: any, suff: any): any {
        const key = pref + '#' + suff;
        return this.lookup.has(key) ? this.lookup.get(key) : -1;
    }
}
