// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

function removeVowels(s: string): string {
    return s.replace(/[aeiou]/g, "");
}
