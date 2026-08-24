// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

export function areSentencesSimilar(sentence1: string[], sentence2: string[], similarPairs: string[][]): boolean {
    if (sentence1.length !== sentence2.length) return false;
    const pairs = new Set();
    for (const pair of similarPairs) {
        pairs.add(pair[0] + '#' + pair[1]);
        pairs.add(pair[1] + '#' + pair[0]);
    }
    for (let i = 0; i < sentence1.length; i++) {
        if (sentence1[i] !== sentence2[i] && !pairs.has(sentence1[i] + '#' + sentence2[i])) return false;
    }
    return true;
}
