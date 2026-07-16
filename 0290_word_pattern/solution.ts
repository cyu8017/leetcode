// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

export function wordPattern(pattern: string, s: string): boolean {
    const words = s.split(" ");
    if (pattern.length !== words.length) {
        return false;
    }
    const charToWord = new Map<string, string>();
    const wordToChar = new Map<string, string>();
    for (let index = 0; index < pattern.length; index += 1) {
        const char = pattern[index];
        const word = words[index];
        if (charToWord.has(char)) {
            if (charToWord.get(char) !== word) {
                return false;
            }
        } else if (wordToChar.has(word)) {
            return false;
        } else {
            charToWord.set(char, word);
            wordToChar.set(word, char);
        }
    }
    return true;
}
