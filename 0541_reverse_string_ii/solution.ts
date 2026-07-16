// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

export class Solution {
    reverseStr(s: string, k: number): string {
        const chars = s.split("");
        for (let start = 0; start < chars.length; start += 2 * k) {
            let left = start;
            let right = Math.min(start + k, chars.length) - 1;
            while (left < right) {
                [chars[left], chars[right]] = [chars[right], chars[left]];
                left += 1;
                right -= 1;
            }
        }
        return chars.join("");
    }
}
