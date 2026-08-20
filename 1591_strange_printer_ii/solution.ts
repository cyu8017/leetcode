// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/
// @ts-nocheck

function isPrintable(targetGrid: number[][]): boolean {
    const colors = new Set();
    for (const row of targetGrid) for (const x of row) colors.add(x);
    const bounds = {};
    for (const c of colors) bounds[c] = [1e9, 1e9, -1, -1];
    for (let r = 0; r < targetGrid.length; r++) {
        for (let col = 0; col < targetGrid[0].length; col++) {
            const c = targetGrid[r][col];
            const b = bounds[c];
            b[0] = Math.min(b[0], r);
            b[1] = Math.min(b[1], col);
            b[2] = Math.max(b[2], r);
            b[3] = Math.max(b[3], col);
        }
    }
    const graph = {};
    const indegree = {};
    for (const c of colors) {
        graph[c] = new Set();
        indegree[c] = 0;
    }
    for (const c of colors) {
        const [r1, c1, r2, c2] = bounds[c];
        for (let r = r1; r <= r2; r++) {
            for (let col = c1; col <= c2; col++) {
                const other = targetGrid[r][col];
                if (other !== c && !graph[c].has(other)) {
                    graph[c].add(other);
                    indegree[other]++;
                }
            }
        }
    }
    const queue = [];
    for (const c of colors) if (indegree[c] === 0) queue.push(c);
    let seen = 0;
    while (queue.length) {
        const c = queue.shift();
        seen++;
        for (const nxt of graph[c]) {
            indegree[nxt]--;
            if (indegree[nxt] === 0) queue.push(nxt);
        }
    }
    return seen === colors.size;
}
