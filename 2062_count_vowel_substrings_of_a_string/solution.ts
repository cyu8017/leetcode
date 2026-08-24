// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

export function countVowelSubstrings(word: string): number {
    const isVowel = (c) => "aeiou".includes(c);
    let ans = 0;
    const n = word.length;
    for (let i = 0; i < n; i++) {
        const seen = new Set();
        for (let j = i; j < n && isVowel(word[j]); j++) {
            seen.add(word[j]);
            if (seen.size === 5) ans++;
        }
    }
    return ans;
}
