// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

function findInteger(k: number, digit1: number, digit2: number): number {
    const digits = [...new Set([digit1, digit2])].sort((a, b) => a - b);
    const q: number[] = [];
    const seen = new Set<number>();
    for (const d of digits) {
        if (d !== 0) {
            q.push(d);
            seen.add(d);
        }
    }
    if (!q.length) return -1;
    const LIMIT = 2147483647;
    for (let qi = 0; qi < q.length; qi++) {
        const x: number = q[qi];
        if (x > k && x % k === 0) return x;
        for (const d of digits) {
            const nx: number = x * 10 + d;
            if (nx <= LIMIT && !seen.has(nx)) {
                seen.add(nx);
                q.push(nx);
            }
        }
    }
    return -1;
}
