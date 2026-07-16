// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

export class Solution {
    repeatedSubstringPattern(s: string): boolean {
        const doubled = s + s;
        return doubled.slice(1, -1).includes(s);
    }
}
