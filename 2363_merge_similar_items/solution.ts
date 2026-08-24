// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

export function mergeSimilarItems(items1: number[][], items2: number[][]): number[][] {
    const mp = new Map();
    for (const it of items1) mp.set(it[0], (mp.get(it[0]) || 0) + it[1]);
    for (const it of items2) mp.set(it[0], (mp.get(it[0]) || 0) + it[1]);
    return [...mp.entries()].sort((a, b) => a[0] - b[0]).map(([k, v]) => [k, v]);
}
