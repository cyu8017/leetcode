// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

function mergeAlternately(word1: string, word2: string): string {
    let i = 0;
    let j = 0;
    const out: string[] = [];
    while (i < word1.length || j < word2.length) {
        if (i < word1.length) {
            out.push(word1[i]);
            i++;
        }
        if (j < word2.length) {
            out.push(word2[j]);
            j++;
        }
    }
    return out.join("");
}
