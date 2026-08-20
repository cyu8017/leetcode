// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

function smallestStringWithSwaps(s: string, pairs: number[][]): string {
    const parent = Array.from({ length: s.length }, (_, i) => i);
    const find = (x) => {
        while (x !== parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    for (const [a, b] of pairs) parent[find(a)] = find(b);
    const groups = new Map();
    for (let i = 0; i < s.length; i++) {
        const r = find(i);
        if (!groups.has(r)) groups.set(r, []);
        groups.get(r).push(s[i]);
    }
    for (const chars of groups.values()) chars.sort((a, b) => b.localeCompare(a));
    let ans = '';
    for (let i = 0; i < s.length; i++) ans += groups.get(find(i)).pop();
    return ans;
}
