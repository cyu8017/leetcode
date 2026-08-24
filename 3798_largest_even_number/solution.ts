// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

export function largestEven(s: any): any {
    while (s.length > 0 && s[s.length - 1] === '1') s = s.substring(0, s.length - 1);
    return s;
}
