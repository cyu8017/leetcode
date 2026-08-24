// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

export function minSwapsCouples(row: number[]): number {
    const pos = new Map();
    for (let i = 0; i < row.length; i++) pos.set(row[i], i);
    let swaps = 0;
    for (let i = 0; i < row.length; i += 2) {
        const partner = row[i] ^ 1;
        if (row[i + 1] === partner) continue;
        const j = pos.get(partner);
        pos.set(row[i + 1], j);
        row[j] = row[i + 1];
        row[i + 1] = partner;
        pos.set(partner, i + 1);
        swaps++;
    }
    return swaps;
}
