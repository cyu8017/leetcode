// LeetCode 0399 - Evaluate Division
export function calcEquation(
    equations: string[][],
    values: number[],
    queries: string[][],
): number[] {
    const graph = new Map<string, Map<string, number>>();

    for (let index = 0; index < equations.length; index += 1) {
        const [dividend, divisor] = equations[index];
        const value = values[index];
        if (!graph.has(dividend)) graph.set(dividend, new Map());
        if (!graph.has(divisor)) graph.set(divisor, new Map());
        graph.get(dividend)!.set(divisor, value);
        graph.get(divisor)!.set(dividend, 1 / value);
    }

    function dfs(start: string, end: string, visited: Set<string>): number {
        if (!graph.has(start) || !graph.has(end)) return -1.0;
        if (start === end) return 1.0;
        visited.add(start);
        for (const [neighbor, weight] of graph.get(start)!) {
            if (visited.has(neighbor)) continue;
            const result = dfs(neighbor, end, visited);
            if (result !== -1.0) return weight * result;
        }
        return -1.0;
    }

    return queries.map(([start, end]) => dfs(start, end, new Set()));
}
