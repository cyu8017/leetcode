// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

export class Solution {
    findAllConcatenatedWordsInADict(words: string[]): string[] {
        const sorted = [...words].sort((a, b) => a.length - b.length);
        const wordSet = new Set(sorted);
        const result: string[] = [];

        const canForm = (word: string, dictionary: Set<string>): boolean => {
            if (!word) return true;
            const length = word.length;
            const dp = new Array<boolean>(length + 1).fill(false);
            dp[0] = true;
            for (let end = 1; end <= length; end += 1) {
                for (let start = 0; start < end; start += 1) {
                    if (dp[start] && dictionary.has(word.slice(start, end))) {
                        dp[end] = true;
                        break;
                    }
                }
            }
            return dp[length];
        };

        for (const word of sorted) {
            wordSet.delete(word);
            if (canForm(word, wordSet)) {
                result.push(word);
            }
            wordSet.add(word);
        }
        return result;
    }
}
