// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

export function canReorderDoubled(arr: number[]): boolean {
    const count = new Map();
    for (const x of arr) count.set(x, (count.get(x) || 0) + 1);
    const keys = [...count.keys()].sort((a, b) => Math.abs(a) - Math.abs(b));
    for (const x of keys) {
        const need = count.get(x);
        if (need === 0) continue;
        if ((count.get(2 * x) || 0) < need) return false;
        count.set(2 * x, count.get(2 * x) - need);
    }
    return true;
}
