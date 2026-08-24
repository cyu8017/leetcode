// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

export function removeStones(stones: number[][]): number {
    const parent = new Map();
    const find = (x) => {
        if (!parent.has(x)) parent.set(x, x);
        if (parent.get(x) !== x) parent.set(x, find(parent.get(x)));
        return parent.get(x);
    };
    const unite = (a, b) => { parent.set(find(a), find(b)); };
    for (const s of stones) unite(s[0], ~s[1]);
    const roots = new Set();
    for (const s of stones) roots.add(find(s[0]));
    return stones.length - roots.size;
}
