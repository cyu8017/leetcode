// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

export class ValidWordAbbr {
    private groups: Map<string, Set<string>>;

    constructor(dictionary: string[]) {
        this.groups = new Map();
        for (const word of dictionary) {
            const key = ValidWordAbbr.abbreviate(word);
            if (!this.groups.has(key)) {
                this.groups.set(key, new Set());
            }
            this.groups.get(key)!.add(word);
        }
    }

    isUnique(word: string): boolean {
        const key = ValidWordAbbr.abbreviate(word);
        const words = this.groups.get(key);
        return !words || (words.size === 1 && words.has(word));
    }

    private static abbreviate(word: string): string {
        if (word.length <= 2) {
            return word;
        }
        return `${word[0]}${word.length - 2}${word[word.length - 1]}`;
    }
}
