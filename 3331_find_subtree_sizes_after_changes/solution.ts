// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

export function findSubtreeSizes(parent: any, s: any): any {
    const n = parent.length;
    const g = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) g[parent[i]].push(i);
    const newParent = parent.slice();
    const last = new Array(26).fill(-1);
    const dfs1 = (u) => {
        const c = s.charCodeAt(u) - 97;
        const prev = last[c];
        if (prev !== -1) newParent[u] = prev;
        last[c] = u;
        for (const v of g[u]) dfs1(v);
        last[c] = prev;
    };
    dfs1(0);
    const ng = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) ng[newParent[i]].push(i);
    const ans = new Array(n);
    const dfs2 = (u) => {
        let sz = 1;
        for (const v of ng[u]) sz += dfs2(v);
        return ans[u] = sz;
    };
    dfs2(0);
    return ans;
}
