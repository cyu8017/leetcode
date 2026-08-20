// LeetCode 1967 - Number of Strings That Appear as Substrings in Word
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

function numOfStrings(patterns: string[], word: string): number {
    return patterns.filter((p: any) => word.includes(p)).length;
}
