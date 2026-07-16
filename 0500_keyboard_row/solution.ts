// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

export class Solution {
    findWords(words: string[]): string[] {
        const rows = [
            new Set("qwertyuiop".split("")),
            new Set("asdfghjkl".split("")),
            new Set("zxcvbnm".split("")),
        ];
        const onOneRow = (word: string): boolean => {
            const letters = new Set([...word.toLowerCase()].filter((ch) => /[a-z]/.test(ch)));
            return rows.some((row) => [...letters].every((letter) => row.has(letter)));
        };
        return words.filter(onOneRow);
    }
}
