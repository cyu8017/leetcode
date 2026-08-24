// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

export function digitSum(s: string, k: number): string {
    while (s.length > k) {
        let next = '';
        for (let i = 0; i < s.length; i += k) {
            let sum = 0;
            const end = Math.min(i + k, s.length);
            for (let j = i; j < end; j++) sum += s.charCodeAt(j) - 48;
            next += String(sum);
        }
        s = next;
    }
    return s;
}
