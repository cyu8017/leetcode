"use strict";
function minReorder(n, connections) {
    const graph = Array.from({ length: n }, (), any), any;
    [];
    ;
    for (const [from, to] of connections) {
        graph[from].push([to, 1]);
        graph[to].push([from, 0]);
    }
    let changes = 0;
    const seen = new Set([0]), stack = [0];
    while (stack.length) {
        const node = stack.pop();
        for (const [next, cost] of graph[node])
            if (!seen.has(next)) {
                seen.add(next);
                changes += cost;
                stack.push(next);
            }
    }
    return changes;
}
