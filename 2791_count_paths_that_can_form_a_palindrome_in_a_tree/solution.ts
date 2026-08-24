// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

export function countPalindromePaths(parent: number[], s: string): number {
    const n = parent.length;
    const g = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) g[parent[i]].push(i);
    const freq = new Map([[0, 1]]);
    let ans = 0;
    const dfs = (u, mask) => {
        for (const v of g[u]) {
            const nm = mask ^ (1 << (s.charCodeAt(v) - 97));
            ans += freq.get(nm) || 0;
            for (let b = 0; b < 26; b++) ans += freq.get(nm ^ (1 << b)) || 0;
            freq.set(nm, (freq.get(nm) || 0) + 1);
            dfs(v, nm);
        }
    };
    dfs(0, 0);
    return ans;
}
