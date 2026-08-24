// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

const MOD = 1000000007;

function multiply(a: any, b: any): any {
    const c = [[0, 0], [0, 0]];
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            for (let k = 0; k < 2; k++) {
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
            }
        }
    }
    return c;
}
export function gatePathXor(n: any, parent: any, gates: any, queries: any): any {
    let logn = 1;
    while ((1 << logn) <= n) logn++;
    const up = Array.from({length: logn}, () => new Array(n).fill(0));
    const product = Array.from({length: logn}, () => Array.from({length: n}, () => null));
    const children = Array.from({length: n}, () => []);
    for (let node = 1; node < n; node++) children[parent[node]].push(node);
    const depth = new Array(n).fill(0);
    const order = [0];
    for (let i = 0; i < order.length; i++) {
        const u = order[i];
        for (const v of children[u]) {
            depth[v] = depth[u] + 1;
            order.push(v);
        }
    }
    for (let u = 0; u < n; u++) {
        up[0][u] = (u === 0) ? 0 : parent[u];
        product[0][u] = [
            [gates[u][1], gates[u][2]],
            [gates[u][2], gates[u][0]]
        ];
    }
    for (let level = 1; level < logn; level++) {
        for (let u = 0; u < n; u++) {
            const mid = up[level - 1][u];
            up[level][u] = up[level - 1][mid];
            product[level][u] = multiply(product[level - 1][u], product[level - 1][mid]);
        }
    }
    let answer = 0;
    for (const query of queries) {
        const ancestor = lca(query[0], query[2], depth, up, logn);
        const alice = ways(query[0], query[1], depth[query[0]] - depth[ancestor], up, product);
        const bob = ways(query[2], query[3], depth[query[2]] - depth[ancestor], up, product);
        const total = Number((BigInt(alice) * BigInt(bob)) % BigInt(MOD));
        answer ^= total;
    }
    return answer;
}
function liftNode(node: any, distance: any, up: any): any {
    for (let level = 0; distance > 0; level++) {
        if ((distance & 1) !== 0) node = up[level][node];
        distance >>= 1;
    }
    return node;
}
function lca(a: any, b: any, depth: any, up: any, logn: any): any {
    if (depth[a] > depth[b]) a = liftNode(a, depth[a] - depth[b], up);
    else if (depth[b] > depth[a]) b = liftNode(b, depth[b] - depth[a], up);
    if (a === b) return a;
    for (let level = logn - 1; level >= 0; level--) {
        if (up[level][a] !== up[level][b]) {
            a = up[level][a];
            b = up[level][b];
        }
    }
    return up[0][a];
}
function ways(node: any, card: any, distance: any, up: any, product: any): any {
    let vector = [0, 0];
    vector[card] = 1;
    for (let level = 0; distance > 0; level++) {
        if ((distance & 1) !== 0) {
            const matrix = product[level][node];
            vector = [
                (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % MOD,
                (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % MOD
            ];
            node = up[level][node];
        }
        distance >>= 1;
    }
    return (vector[0] + vector[1]) % MOD;
}
