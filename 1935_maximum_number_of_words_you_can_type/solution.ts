// LeetCode 1935 - Maximum Number of Words You Can Type
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

function canBeTypedWords(text: string, brokenLetters: string): number {
    const broken = new Set(brokenLetters);
    return text.split(" ").filter((w: any) => ![...w].some((ch: any) => broken.has(ch))).length;
}
