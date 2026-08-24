// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

export function smallestMissingValueSubtree(parents: number[], nums: number[]): number[] {
    const n = parents.length;
    const children = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) children[parents[i]].push(i);
    const ans = new Array(n).fill(1);
    let one = -1;
    for (let i = 0; i < n; i++) if (nums[i] === 1) { one = i; break; }
    if (one < 0) return ans;
    const seen = new Set();
    const collect = (u) => {
        if (seen.has(nums[u])) return;
        seen.add(nums[u]);
        for (const v of children[u]) collect(v);
    };
    let miss = 1, node = one, prev = -1;
    while (node !== -1) {
        for (const v of children[node]) if (v !== prev) collect(v);
        seen.add(nums[node]);
        while (seen.has(miss)) miss++;
        ans[node] = miss;
        prev = node;
        node = parents[node];
    }
    return ans;
}
