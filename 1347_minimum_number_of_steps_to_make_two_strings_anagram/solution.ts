// LeetCode 1347 - Minimum Number Of Steps To Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

function minSteps(s: string, t: string): number {
    const count = Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        count[s.charCodeAt(i) - 97]++;
        count[t.charCodeAt(i) - 97]--;
    }
    return count.reduce((sum, c: any): any => sum + Math.max(c, 0), 0);
}
