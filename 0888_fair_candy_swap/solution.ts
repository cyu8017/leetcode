// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

export function fairCandySwap(aliceSizes: number[], bobSizes: number[]): number[] {
    let sumA = 0, sumB = 0;
    for (const a of aliceSizes) sumA += a;
    for (const b of bobSizes) sumB += b;
    const diff = (sumA - sumB) / 2;
    const bob = new Set(bobSizes);
    for (const a of aliceSizes) {
        if (bob.has(a - diff)) return [a, a - diff];
    }
    return [];
}
