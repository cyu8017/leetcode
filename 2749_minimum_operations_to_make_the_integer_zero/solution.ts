// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

export function makeTheIntegerZero(num1: number, num2: number): number {
    const popcount = (x) => {
        let c = 0n;
        let v = BigInt(x);
        while (v > 0n) {
            c += v & 1n;
            v >>= 1n;
        }
        return Number(c);
    };
    for (let k = 1; k <= 60; k++) {
        const rem = BigInt(num1) - BigInt(k) * BigInt(num2);
        if (rem < BigInt(k)) continue;
        if (popcount(rem) <= k) return k;
    }
    return -1;
}
