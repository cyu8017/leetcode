// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

export function findAnswer(parent: any, s: any): any {
    const n = parent.length;
    const g = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) g[parent[i]].push(i);
    const ans = new Array(n);
    const isPal = (t) => {
        for (let i = 0, j = t.length - 1; i < j; i++, j--) {
            if (t[i] !== t[j]) return false;
        }
        return true;
    };
    const dfsStr = (u) => {
        let out = '';
        for (const v of g[u]) out += dfsStr(v);
        out += s[u];
        ans[u] = isPal(out);
        return out;
    };
    dfsStr(0);
    return ans;
}
