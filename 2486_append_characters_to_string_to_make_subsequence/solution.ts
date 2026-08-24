// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

export function appendCharacters(s: string, t: string): number {
    let j = 0;
    for (let i = 0; i < s.length && j < t.length; i++) {
        if (s[i] === t[j]) j++;
    }
    return t.length - j;
}
