// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

function gardenNoAdj(n: number, paths: number[][]): number[] {
    const graph: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of paths) {
        graph[a].push(b);
        graph[b].push(a);
    }
    const ans = new Array(n + 1).fill(0);
    for (let garden = 1; garden <= n; garden++) {
        const used = new Set(graph[garden].map((nei) => ans[nei]));
        for (let c = 1; c <= 4; c++) {
            if (!used.has(c)) {
                ans[garden] = c;
                break;
            }
        }
    }
    return ans.slice(1);
}
