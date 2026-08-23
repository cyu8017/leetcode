// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

/**
 * @param {number[]} aliceSizes
 * @param {number[]} bobSizes
 * @return {number[]}
 */
var fairCandySwap = function(aliceSizes, bobSizes) {
    let sumA = 0, sumB = 0;
    for (const a of aliceSizes) sumA += a;
    for (const b of bobSizes) sumB += b;
    const diff = (sumA - sumB) / 2;
    const bob = new Set(bobSizes);
    for (const a of aliceSizes) {
        if (bob.has(a - diff)) return [a, a - diff];
    }
    return [];
};
