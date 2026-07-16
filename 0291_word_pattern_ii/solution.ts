// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

export function wordPatternMatch(pattern: string, s: string): boolean {
    const charToWord = new Map<string, string>();
    const wordToChar = new Map<string, string>();

    function backtrack(patternIndex: number, stringIndex: number): boolean {
        if (patternIndex === pattern.length) {
            return stringIndex === s.length;
        }
        const char = pattern[patternIndex];
        if (charToWord.has(char)) {
            const word = charToWord.get(char) as string;
            if (!s.startsWith(word, stringIndex)) {
                return false;
            }
            return backtrack(patternIndex + 1, stringIndex + word.length);
        }
        for (let end = stringIndex + 1; end <= s.length; end += 1) {
            const word = s.slice(stringIndex, end);
            if (wordToChar.has(word)) {
                continue;
            }
            charToWord.set(char, word);
            wordToChar.set(word, char);
            if (backtrack(patternIndex + 1, end)) {
                return true;
            }
            charToWord.delete(char);
            wordToChar.delete(word);
        }
        return false;
    }

    return backtrack(0, 0);
}
