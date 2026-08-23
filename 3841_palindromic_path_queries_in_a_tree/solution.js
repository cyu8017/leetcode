// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

var palindromicPathQueries = function(n, edges, s, queries) {
    const graph = Array.from({length: n}, () => []);
    for (const edge of edges) {
        graph[edge[0]].push(edge[1]);
        graph[edge[1]].push(edge[0]);
    }
    const parent = new Array(n).fill(-2);
    const depth = new Array(n).fill(0);
    parent[0] = -1;
    const order = [0];
    for (let i = 0; i < order.length; i++) {
        const u = order[i];
        for (const v of graph[u]) {
            if (parent[v] === -2) {
                parent[v] = u;
                depth[v] = depth[u] + 1;
                order.push(v);
            }
        }
    }
    const size = new Array(n).fill(0);
    const heavy = new Array(n).fill(-1);
    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];
        size[u] = 1;
        for (const v of graph[u]) {
            if (parent[v] === u) {
                size[u] += size[v];
                if (heavy[u] === -1 || size[v] > size[heavy[u]]) heavy[u] = v;
            }
        }
    }
    const head = new Array(n).fill(0);
    const position = new Array(n).fill(0);
    const stack = [[0, 0]];
    let nextPosition = 0;
    while (stack.length) {
        const chain = stack.pop();
        for (let u = chain[0]; u !== -1; u = heavy[u]) {
            head[u] = chain[1];
            position[u] = nextPosition++;
            for (const v of graph[u]) {
                if (parent[v] === u && v !== heavy[u]) stack.push([v, v]);
            }
        }
    }
    const bit = new Array(n + 1).fill(0);
    const update = (index, value) => {
        for (index++; index <= n; index += index & -index) bit[index] ^= value;
    };
    const prefix = (index) => {
        let result = 0;
        for (; index > 0; index -= index & -index) result ^= bit[index];
        return result;
    };
    const pathMask = (u, v) => {
        let result = 0;
        while (head[u] !== head[v]) {
            if (depth[head[u]] < depth[head[v]]) { const tmp = u; u = v; v = tmp; }
            result ^= prefix(position[u] + 1) ^ prefix(position[head[u]]);
            u = parent[head[u]];
        }
        if (position[u] > position[v]) { const tmp = u; u = v; v = tmp; }
        return result ^ prefix(position[v] + 1) ^ prefix(position[u]);
    };
    const current = s.split('');
    for (let node = 0; node < n; node++) update(position[node], 1 << (current[node].charCodeAt(0) - 97));
    const answer = [];
    for (const query of queries) {
        const parts = query.split(' ');
        const op = parts[0];
        const node = parseInt(parts[1], 10);
        if (op === 'update') {
            const newCharacter = parts[2][0];
            const delta = (1 << (current[node].charCodeAt(0) - 97)) ^ (1 << (newCharacter.charCodeAt(0) - 97));
            update(position[node], delta);
            current[node] = newCharacter;
        } else {
            const other = parseInt(parts[2], 10);
            const mask = pathMask(node, other);
            answer.push((mask & (mask - 1)) === 0);
        }
    }
    return answer;
};
