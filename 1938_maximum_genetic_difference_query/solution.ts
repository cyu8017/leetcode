// LeetCode 1938 - Maximum Genetic Difference Query
// https://leetcode.com/problems/maximum-genetic-difference-query/

type TrieNode = { child: Array<TrieNode | null>; cnt: number };

function maxGeneticDifference(parents: number[], queries: number[][]): number[] {
    const n = parents.length;
    const children: number[][] = Array.from({ length: n }, () => []);
    let root = 0;
    for (let i = 0; i < n; i++) {
        if (parents[i] === -1) root = i;
        else children[parents[i]].push(i);
    }
    const qmap: number[][][] = Array.from({ length: n }, () => []);
    for (let i = 0; i < queries.length; i++) qmap[queries[i][0]].push([i, queries[i][1]]);
    const ans = new Array(queries.length).fill(0);
    const BITS = 17;
    const makeNode = (): TrieNode => ({ child: [null, null], cnt: 0 });
    const trieRoot = makeNode();
    const trieUpdate = (num: number, delta: number): void => {
        let node = trieRoot;
        for (let b = BITS; b >= 0; b--) {
            const bit = (num >> b) & 1;
            if (!node.child[bit]) node.child[bit] = makeNode();
            node = node.child[bit]!;
            node.cnt += delta;
        }
    };
    const trieMaxXor = (num: number): number => {
        let node: TrieNode = trieRoot, res = 0;
        for (let b = BITS; b >= 0; b--) {
            const bit = (num >> b) & 1;
            const want = 1 - bit;
            if (node.child[want] && node.child[want]!.cnt > 0) {
                res |= 1 << b;
                node = node.child[want]!;
            } else {
                node = node.child[bit]!;
            }
        }
        return res;
    };
    const dfs = (u: number): void => {
        trieUpdate(u, 1);
        for (const [qi, val] of qmap[u]) ans[qi] = trieMaxXor(val);
        for (const v of children[u]) dfs(v);
        trieUpdate(u, -1);
    };
    dfs(root);
    return ans;
}
