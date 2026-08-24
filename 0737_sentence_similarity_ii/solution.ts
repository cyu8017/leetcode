// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

export function areSentencesSimilarTwo(sentence1: string[], sentence2: string[], similarPairs: string[][]): boolean {
    if (sentence1.length !== sentence2.length) return false;
    const parent = new Map();
    const find = (x) => {
        if (!parent.has(x)) parent.set(x, x);
        while (parent.get(x) !== x) {
            parent.set(x, parent.get(parent.get(x)));
            x = parent.get(x);
        }
        return x;
    };
    const unite = (a, b) => { parent.set(find(a), find(b)); };
    for (const pair of similarPairs) unite(pair[0], pair[1]);
    for (let i = 0; i < sentence1.length; i++) {
        if (find(sentence1[i]) !== find(sentence2[i])) return false;
    }
    return true;
}
