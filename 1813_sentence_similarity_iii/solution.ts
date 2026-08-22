// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

function areSentencesSimilar(sentence1: string, sentence2: string): boolean {
    const words1 = sentence1.split(' ');
    const words2 = sentence2.split(' ');
    const n1 = words1.length, n2 = words2.length;
    let i = 0;
    while (i < n1 && i < n2 && words1[i] === words2[i]) i += 1;
    if (i === n1 || i === n2) return true;
    let j1 = n1 - 1, j2 = n2 - 1;
    while (j1 >= i && j2 >= i && words1[j1] === words2[j2]) {
        j1 -= 1;
        j2 -= 1;
    }
    return j1 < i || j2 < i;
}
