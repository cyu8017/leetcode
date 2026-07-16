// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

export function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) {
        return false;
    }
    const counts = new Array<number>(26).fill(0);
    for (let index = 0; index < s.length; index++) {
        counts[s.charCodeAt(index) - 97]++;
        counts[t.charCodeAt(index) - 97]--;
    }
    return counts.every((count) => count === 0);
}
