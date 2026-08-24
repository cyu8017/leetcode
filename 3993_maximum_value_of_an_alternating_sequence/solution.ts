// LeetCode 3993 - Maximum Value of an Alternating Sequence
// https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

export function maximumValue(n: any, s: any, m: any): any {
        if (n == 1) return s;
        return s + (n / 2) * (m - 1) + 1;
    
}
