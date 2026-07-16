// LeetCode 0151 - Reverse Words in a String
// https://leetcode.com/problems/reverse-words-in-a-string/

export function reverseWords(s: string): string {
    return s.trim().split(/\s+/).reverse().join(" ");
}