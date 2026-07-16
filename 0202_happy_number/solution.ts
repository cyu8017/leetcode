// LeetCode 0202 - Happy Number
// https://leetcode.com/problems/happy-number/

export function isHappy(n: number): boolean {
    const seen = new Set<number>();

    const nextValue = (value: number): number => {
        let total = 0;
        while (value > 0) {
            const digit = value % 10;
            total += digit * digit;
            value = Math.floor(value / 10);
        }
        return total;
    };

    while (n !== 1 && !seen.has(n)) {
        seen.add(n);
        n = nextValue(n);
    }
    return n === 1;
}