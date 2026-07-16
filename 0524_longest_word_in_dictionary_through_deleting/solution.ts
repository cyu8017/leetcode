// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

export class Solution {
    findLongestWord(s: string, dictionary: string[]): string {
        const isSubsequence = (word: string): boolean => {
            let index = 0;
            for (const char of s) {
                if (index < word.length && word[index] === char) index += 1;
            }
            return index === word.length;
        };
        let best = "";
        for (const word of dictionary) {
            if (isSubsequence(word) && (word.length > best.length || (word.length === best.length && word < best))) {
                best = word;
            }
        }
        return best;
    }
}
