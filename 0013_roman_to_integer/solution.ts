// LeetCode 0013 - Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

export function romanToInt(s: string): number {
    const values: Record<string, number> = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
    let total = 0;
    let prev = 0;

    for (let i = s.length - 1; i >= 0; i--) {
        const curr = values[s[i]];
        if (curr < prev) {
            total -= curr;
        } else {
            total += curr;
        }
        prev = curr;
    }

    return total;
}
