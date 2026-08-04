var findCriticalAndPseudoCriticalEdges = function(n, edges) {
    const sorted = edges.map((edge, index) => [...edge, index]).sort((a, b) => a[2] - b[2]);
    const mst = (skip = -1, force = -1) => {
        const parent = Array.from({ length: n }, (_, i) => i);
        const find = node => parent[node] === node ? node : parent[node] = find(parent[node]);
        let total = 0, used = 0;
        const join = edge => {
            const [from, to, weight] = sorted[edge], a = find(from), b = find(to);
            if (a === b) return;
            parent[a] = b;
            total += weight;
            used++;
        };
        if (force !== -1) join(force);
        for (let i = 0; i < sorted.length; i++) if (i !== skip && i !== force) join(i);
        return used === n - 1 ? total : Infinity;
    };
    const baseline = mst(), critical = [], pseudo = [];
    for (let i = 0; i < sorted.length; i++) {
        if (mst(i) > baseline) critical.push(sorted[i][3]);
        else if (mst(-1, i) === baseline) pseudo.push(sorted[i][3]);
    }
    return [critical.sort((a, b) => a - b), pseudo.sort((a, b) => a - b)];
};
