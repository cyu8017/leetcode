// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

function isVowel(c: any): any {
    return c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u';
}export function trimTrailingVowels(s: any): any {
    let i = s.length - 1;
    while (i >= 0 && isVowel(s[i])) i--;
    return s.substring(0, i + 1);
}
