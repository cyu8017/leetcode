// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

function isSumEqual(firstWord: string, secondWord: string, targetWord: string): boolean {
    const value = (word: string) => {
        let s = "";
        for (const ch of word) s += String(ch.charCodeAt(0) - 97);
        return Number(s);
    };
    return value(firstWord) + value(secondWord) === value(targetWord);
}
