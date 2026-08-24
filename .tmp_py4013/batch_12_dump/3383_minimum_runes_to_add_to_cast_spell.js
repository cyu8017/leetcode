// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

var minRunesToAdd = function(n, crystals, flowFrom, flowTo) {
    const g = Array.from({length: n}, () => []);
    const rg = Array.from({length: n}, () => []);
    for (let i = 0; i < flowFrom.length; i++) {
        const a = flowFrom[i], b = flowTo[i];
        g[a].push(b);
        rg[b].push(a);
    }
    const vis = new Array(n).fill(false);
    const order = [];
    const dfs1 = (u) => {
        vis[u] = true;
        for (const v of g[u]) if (!vis[v]) dfs1(v);
        order.push(u);
    };
    for (let i = 0; i < n; i++) if (!vis[i]) dfs1(i);
    const comp = new Array(n).fill(-1);
    let cid = 0;
    const dfs2 = (u) => {
        comp[u] = cid;
        for (const v of rg[u]) if (comp[v] === -1) dfs2(v);
    };
    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];
        if (comp[u] === -1) {
            dfs2(u);
            cid++;
        }
    }
    const hasCrystal = new Array(cid).fill(false);
    for (const c of crystals) hasCrystal[comp[c]] = true;
    const indeg = new Array(cid).fill(0);
    for (let u = 0; u < n; u++) {
        for (const v of g[u]) {
            if (comp[u] !== comp[v]) indeg[comp[v]]++;
        }
    }
    let ans = 0;
    for (let i = 0; i < cid; i++) {
        if (indeg[i] === 0 && !hasCrystal[i]) ans++;
    }
    return ans;
};
