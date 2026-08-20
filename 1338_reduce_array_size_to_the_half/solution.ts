// LeetCode 1338 - Reduce Array Size To The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

function minSetSize(arr: number[]): number {
    const counts = new Map();
    for (const value of arr) counts.set(value, (counts.get(value) || 0) + 1);
    const freqs = [...counts.values()].sort((a, b: any): any => b - a);
    let removed = 0;
    for (let i = 0; i < freqs.length; i++) {
        removed += freqs[i];
        if (removed * 2 >= arr.length) return i + 1;
    }
    return 0;
}
