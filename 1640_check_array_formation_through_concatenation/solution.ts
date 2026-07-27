// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

function canFormArray(arr: number[], pieces: number[][]): boolean {
    const byFirst = new Map<number, number[]>();
    for (const p of pieces) byFirst.set(p[0], p);
    let i = 0;
    while (i < arr.length) {
        if (!byFirst.has(arr[i])) return false;
        const p = byFirst.get(arr[i])!;
        for (let j = 0; j < p.length; j++) if (arr[i + j] !== p[j]) return false;
        i += p.length;
    }
    return true;
}
